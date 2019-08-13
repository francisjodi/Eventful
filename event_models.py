from google.appengine.ext import ndb

class Event(ndb.Model):
    event_name =  ndb.StringProperty(required=True)
    location =  ndb.StringProperty(required=True)
    organization_name =  ndb.StringProperty(required=True)
    date_and_time =  ndb.DateTimeProperty()
    additional_info =  ndb.StringProperty(required=False)
    category =  ndb.StringProperty(required=True)
    college_name =  ndb.StringProperty(required=True)
