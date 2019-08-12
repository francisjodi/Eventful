from google.appengine.ext import ndb

class Event(ndb.Model):
    event_name =  ndb.StringProperty(required=True)
    location =  ndb.StringProperty(required=True)
    organization_name =  ndb.StringProperty(required=True)
    date_and_time =  ndb.DateTimeProperty(required=True)
    additional_info =  ndb.StringProperty(required=True)
    category =  ndb.StringProperty(required=True, choices=["All", "Academic", "Athletics", "Arts", "Service", "Other"])
    college_name =  ndb.Property(required=True, choices=["Loyola Marymount University", "University of California Los Angeles", "University of Southern California", "Pepperdine University"])


class Teacher(ndb.Model):
    name = ndb.StringProperty(required=True)
    years_experience = ndb.IntegerProperty(default=1)
    classes_taught = ndb.KeyProperty(Course, repeated=True)
