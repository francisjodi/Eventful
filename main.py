import os
import json
import webapp2
import jinja2
from urllib import urlencode
from google.appengine.api import urlfetch
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
        template = jinja_env.get_template('templates/signin.html')
        self.response.write(template.render())
    def post(self):
        filter = self.request.get('filter')
        template = jinja_env.get_template('templates/signin.html')
        self.response.write(template.render({'response': response}))

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
        self.response.write(template.render())

class CalendarHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('templates/calendar.html')
        self.response.write(template.render())

class SearchHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('templates/home.html')
        self.response.write(template.render())
    def post(self):
        filter = self.request.get('filter')
        template = jinja_env.get_template('templates/home.html')
        #self.response.write(template.render({ 'response': response }))


class AddEventHandler(webapp2.RequestHandler):
    def post(self):
        filter = self.request.get('filter')
        template = jinja_env.get_template('templates/addevent.html')
        #self.response.write(template.render({ 'response': response }))

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
