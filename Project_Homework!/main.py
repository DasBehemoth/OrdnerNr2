#!/usr/bin/env python
import os
import jinja2
import webapp2
import random
import model
import datetime
from google.appengine.api import users

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

        format_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        params["format_datetime"] = format_datetime

        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


Messages = []


class MainHandler(BaseHandler):
    def get(self):
        messages = model.Message.query(model.Message.deleted != True).fetch()
        messages = sorted(messages, key=lambda x: x.name) # sortiert jetzt nach name mit [::-1]  von z bis a
        return self.render_template("startseite.html", params={"messages": messages})

    def post(self):
        name = self.request.get("name")
        message_text = self.request.get("message_text")
        email = self.request.get("email")
        message = model.Message(message_text=message_text, name=name, email=email)
        message.put()
        return self.redirect_to("startseite")


class ShopHandler(BaseHandler):
    def get(self):
        return self.render_template("shop.html")


class SpiritHandler(BaseHandler):
    def get(self):
        return self.render_template("spiritanimal.html")


class MeHandler(BaseHandler):
    def get(self):
        return self.render_template("aboutme.html")


class ContactHandler(BaseHandler):
    def get(self):
        return self.render_template("contact.html")


class LottoHandler (BaseHandler):
    def get(self):
        my_lotto = random.sample(range(1, 50), 6)
        my_lotto = str(my_lotto)
        return self.render_template("lotto.html", params={"site_my_lotto": my_lotto})

    def post(self):
        my_lotto = random.sample(range(1, 50), 6)
        my_lotto = str(my_lotto)
        has_guessed = True
        secret = 42
        number = self.request.get("number")
        number = int(number or 0)
        is_guessed = secret == number
        answer = self.request.get("answer")
        return self.render_template("lotto.html", params={"site_my_lotto": my_lotto, "is_guessed": is_guessed, "has_guessed": has_guessed, "answer":answer, "number": number})

class EditMessageHandler(BaseHandler):
    def get(self, message_id):
        message = model.Message.get_by_id(int(message_id))
        return self.render_template("edit_message.html", params={"message": message})

    def post(self,message_id):
        message = model.Message.get_by_id(int(message_id))
        message.message_text = self.request.get("message_text")
        message.email = self.request.get ("email")
        message.name = self.request.get("name")
        message.put()
        return self.redirect_to("startseite")


class DeleteMessageHandler(BaseHandler):
    def get(self, message_id):
        message = model.Message.get_by_id(int(message_id))
        return self.render_template("delete_message.html", params={"message": message})

    def post(self, message_id):
        message = model.Message.get_by_id(int(message_id))
        # message.key.delete()
        message.deleted = True
        message.put()
        return self.redirect_to("startseite")


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler, name="startseite"),
    webapp2.Route('/shop', ShopHandler),
    webapp2.Route('/aboutme', MeHandler),
    webapp2.Route('/contact', ContactHandler),
    webapp2.Route('/lotto', LottoHandler),
    webapp2.Route('/spiritanimal', SpiritHandler),
    webapp2.Route('/delete_message', DeleteMessageHandler),
    webapp2.Route('/edit_message', EditMessageHandler),
    webapp2.Route('/message/<message_id:\d+>/edit', EditMessageHandler),
    webapp2.Route('/message/<message_id:\d+>/delete', DeleteMessageHandler)
], debug=True)


def main():
    from paste import httpserver
    httpserver.serve(app, host='0.0.0.0', port='8080')


if __name__ == '__main__':
    main()
