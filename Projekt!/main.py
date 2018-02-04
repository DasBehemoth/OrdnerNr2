#!/usr/bin/env python
import os
import jinja2
import webapp2
import random
import datetime
import model


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if params is None:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))

Messages = []
class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("hello.html")

My_History = []


class BlogHandler (BaseHandler):

    def get(self):
        global My_History # sagt def dass my history verwedne soll weil auserhalb von funtktion ist
        my_number = random.randint(0, 9)
        curret_datetime = datetime.datetime.now()
        readable_date = curret_datetime.strftime("%y-%m-%d %H:%M:%S") # oft verwendet current_datetime.isoformat()
        My_History.append((readable_date, my_number))
        return self.render_template("blog.html", params={"site_my_number": my_number, "site_date": readable_date, "site_history": My_History})



class LottoHandler (BaseHandler):
    def get(self):
        my_lotto = random.sample(range(1,50),6)
        return self.render_template("lotto.html", params={"site_my_lotto": my_lotto})



class SngHandler (BaseHandler):
    def get(self):
        number = self.request.get("number")
        return self.render_template("sng.html", params={"my_number": number})

    def post(self):
        has_guessed = True
        secret = 7
        number = self.request.get("number")
        number = int(number or 0)
        is_guessed = secret == number
        answer = self.request.get("answer")
        return self.render_template("sng.html", params={"is_guessed": is_guessed, "has_guessed": has_guessed, "answer":answer})

class Shopping_ListHandler (BaseHandler):
    def get (self):
        return self.render_template("shopping_list.html")

class RealBlogHandler(BaseHandler):
    def get(self):
        messages = model.Message.query().fetch()
        return self.render_template("realblog.html", params={"messages": messages})

    def post(self):
        name = self.request.get("name")
        message_text = self.request.get("message_text")
        message = model.Message(message_text=message_text, name=name)
        message.put()
        return self.redirect_to("real_blog")

class EditMessageHandler(BaseHandler):
    def get(self, message_id):
        message = model.Message.get_by_id(message_id)
        return self.render_template("edit_message.html", params={"message":message})


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/blog', BlogHandler),
    webapp2.Route('/lotto', LottoHandler),
    webapp2.Route('/sng', SngHandler),
    webapp2.Route('/shopping_list', Shopping_ListHandler),
    webapp2.Route('/real_blog', Real_blogHandler, name= "real_blog"),
    webapp2.Route('/message/<message_id:\d+>/edit', EditMessageHandler)
], debug=True)
