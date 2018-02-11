#!/usr/bin/env python
import datetime
import os
import random

import jinja2
import webapp2

import model
import helper
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

        user = users.get_current_user()
        params ["logged_in"]= bool(user)
        params ["user"] = user
        params ["login_url"]= users.create_login_url('/')
        params["logout_url"] = users.create_logout_url('/')

        if user:
            visitor = model.User.query(model.User.email == user.nickname()).fetch()
            if not visitor:
                visitor = model.User(email=user.nickname(),
                                     admin = False,
                                     updated = datetime.datetime.utcnow(),
                                     ip_address =self.request.remote_addr)
            else:
                visitor = visitor(0)
                visitor.updated = datetime.datetime.utcnow()
                visitor.last_ip_address = self.request.remote_addr

            address = helper.get_address_from_ip(visitor.ip_address)
            visitor.city=str(address["city"])
            visitor.country_name=str(address["country_name"])
            visitor.zip_code=str(address["zip_code"])
            visitor.latitude=str(address["latitude"])
            visitor.longitude=str(address["longitude"])

            visitor.put()

        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("hello.html")

MY_HISTORY = []


class LottoHandler(BaseHandler):
    def get(self):
        global MY_HISTORY
        current_datetime = datetime.datetime.now()
        current_datetime += datetime.timedelta(hours=1)
        readable_date = current_datetime.isocalendar()
        my_number = random.randint(0,9)

        MY_HISTORY.append((readable_date, my_number))

        return self.render_template("lotto.html",
                                    params={"site_my_number": my_number,
                                            "site_date": readable_date,
                                            "site_history": MY_HISTORY})


class SNGHandler(BaseHandler):
    def get(self):
        return self.render_template("sng.html")

    def post(self):
        has_guessed = True
        secret = 5
        number = self.request.get("number")
        number = int(number or 0)
        is_guessed = secret == number

        return self.render_template("sng.html",
                                    params={"is_guessed": is_guessed,
                                            "has_guessed": has_guessed})


class ShoppinglistHandler(BaseHandler):
    def get(self):
        return self.render_template("shoppinglist.html")


class OptionsGameHandler(BaseHandler):
    def get(self):
        return self.render_template("options_game.html")

    def post(self):
        answer = self.request.get("answer")
        return self.render_template("options_game.html",
                                    params={"answer":answer})


class RealBlogHandler(BaseHandler):
    def get(self):
        messages = model.Message.query(model.Message.deleted != True).fetch()
        messages = sorted(messages, key=lambda x: x.created)[::-1]
        return self.render_template("realblog.html", params={"messages": messages})

    def post(self):
        name = self.request.get("name")
        message_text = self.request.get("message_text")
        message = model.Message(message_text=message_text, name=name)
        message.put()
        return self.redirect_to("realblog")


class EditMessageHandler(BaseHandler):
    def get(self, message_id):
        message = model.Message.get_by_id(message_id)
        return self.render_template("edit_message.html", params={"message": message})
    def post(self, message_id):
        message = model.Message.get_by_id(message_id)
        message.message_text = self.request.get("message_text")
        message.name = self.request.get("name")
        message.put()
        return self.redirect_to("realblog")

class DeleteMessageHandler(BaseHandler):
    def get(self, message_id):
        message = model.Message.get_by_id(int(message_id))
        return self.render_template("delete_message.html", params={"message": message})

    def post(self, message_id):
        message = model.Message.get_by_id(int(message_id))
        # message.key.delete()
        message.deleted = True
        message.put()
        return self.redirect_to("realblog")


class LoginHandler (BaseHandler):

    def get(self):
        user = users.get_current_user()
        if user:
            logged_in = True
            logout_url = users.create_logout_url('/logintest')

            params = {"logged_in": logged_in, "logout_url": logout_url, "user": user}
        else:
            logged_in = False
            login_url = users.create_login_url('/logintest')

            params = {"logged_in": logged_in, "login_url": login_url, "user": user}

        return self.render_template("logintest.html", params)

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/sng', SNGHandler),
    webapp2.Route('/lotto', LottoHandler),
    webapp2.Route('/shoppinglist', ShoppinglistHandler),
    webapp2.Route('/options_game', OptionsGameHandler),
    webapp2.Route('/realblog', RealBlogHandler, name="realblog"),
    webapp2.Route('/message/<message_id:\d+>/edit', EditMessageHandler),
    webapp2.Route('/message/<message_id:\d+>/delete', DeleteMessageHandler),
    webapp2.Route('/logintest', LoginHandler, name='logintest')
], debug=True)


def main():
    from paste import httpserver
    httpserver.serve(app, host='0.0.0.0', port='8080')


if __name__ == '__main__':
    main()
