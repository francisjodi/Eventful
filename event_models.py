from google.appengine.ext import ndb

class Category(ndb.Model):
    category_name = ndb.StringProperty(required=True);

class Event(ndb.Model):
    event_name =  ndb.StringProperty(required=True)
    location =  ndb.StringProperty(required=True)
    organization_name =  ndb.StringProperty(required=True)
    date_and_time =  ndb.DateProperty(required=True)
    time = ndb.TimeProperty(required=True)
    additional_info =  ndb.StringProperty(required=False)
    category =  ndb.StringProperty(required=True)
    college_name =  ndb.StringProperty(required=True)
