
from google.appengine.ext import ndb

class Message (ndb.Model):
    message = ndb.StringProperty()
    name = ndb.StringProperty()



