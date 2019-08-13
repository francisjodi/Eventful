import os
import json
import webapp2
import jinja2
from urllib import urlencode
from google.appengine.api import urlfetch
from google.appengine.api import users
from event_models import Event
from seed_events import seed_data
import datetime

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

def createEvent(name,location,org,category,college,date):
        event = Event(
            event_name=name,
            location=location,
            organization_name=org,
            category=category,
            college_name=college,
            date_and_time = date
        )

        event.put()

class SigninHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        template = jinja_env.get_template('/templates/signin.html')
        if user:
            logout_url = users.create_logout_url('/')
            self.response.write(template.render({
                "loginURL":logout_url
            }))
        else:
            login_URL = users.create_login_url('/')
            self.response.write(template.render({
                "loginURL":login_URL
            }))

    def post(self):
        filter = self.request.get('filter')
        template = jinja_env.get_template('/templates/signin.html')
        self.response.write(template.render({'response':'string'}))


class EventPageHandler(webapp2.RequestHandler):
    def get(self):
        createEvent("basketball game",
            "gym",
             "basketball team",
             "Athletics",
             "Loyola Marymount University",
             datetime.datetime(2019, 9, 10, 15, 30, 0, 0))
        event = Event.query().filter(Event.event_name=="basketball game").get()
        # self.response.write("{} is the date and time".format(event.date_and_time))
        template = jinja_env.get_template('templates/eventpage.html')
        self.response.write(event)


class CalendarHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('/templates/calendar.html')
        self.response.write(template.render())
        

class SearchHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('/templates/home.html')
        self.response.write(template.render())
    def post(self):
        filter = self.request.get('filter')
        template = jinja_env.get_template('/templates/home.html')
        #self.response.write(template.render({ 'response': response }))

class EventPageHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('/templates/eventpage.html')
        self.response.write(template.render())
        
class AddEventHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('/templates/addevent.html')
        self.response.write(template.render())
    def post(self):
        event_name = self.request.get('event_name')
        organization_name = self.request.get('organization_name')
        college_name = self.request.get('college_name')
        category = self.request.get('category')
        location = self.request.get('location')
        date_and_time = map( int, self.request.get('date').split("-"))
        year= date_and_time[0]
        month= date_and_time[1]
        day = date_and_time[2]
        event_key = Event(event_name=event_name,
                    organization_name=organization_name,
                    college_name=college_name,
                    category=category,
                    location=location,
                    date_and_time=datetime.date(year,month,day)
                    ).put()

        event_block = Event.query().order(Event.category).fetch()
        self.response.write(template.render({'event_block' : event_block}))


class LoadDataHandler(webapp2.RequestHandler):
    def get(self):
        seed_data()
        # createEvent("basketball game", "gym", "basketball team", "Athletics", "Loyola Marymount University")


app = webapp2.WSGIApplication([
    ('/', SigninHandler),
    ('/search', SearchHandler),
    ('/calendar', CalendarHandler),
    ('/addevent', AddEventHandler),
    ('/events', EventPageHandler),
    ('/seed-data', LoadDataHandler),
], debug=True)
