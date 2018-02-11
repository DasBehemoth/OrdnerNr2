from google.appengine.ext import ndb


class Message(ndb.Model):
    message_text = ndb.StringProperty()
    name = ndb.StringProperty()
    deleted = ndb.BooleanProperty(default=False)
    created = ndb.DateTimeProperty(auto_now_add=True)

class User(ndb.Model):
    email = ndb.StringProperty()
    admin = ndb.BooleanProperty(default=False)
    updated = ndb.DateTimeProperty(auto_now_add=True)
    ip_address = ndb.StringProperty(default="")
    zip_code= ndb.StringProperty(default="")
    city = ndb.StringProperty(default="")
    country_name = ndb.StringProperty(default="")
    longitude = ndb.StringProperty(default="")
    latitude = ndb.StringProperty(default="")