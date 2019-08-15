import os
import json
import webapp2
import jinja2
from urllib import urlencode
from google.appengine.api import urlfetch
from google.appengine.api import users
from event_models import Event, Category
from seed_events import seed_data
import datetime
import logging

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

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

class particleHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('/templates/particles.html')
        self.response.write(template.render())

class SigninHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        template = jinja_env.get_template('/templates/signin.html')

        if user:
            logout_url = users.create_logout_url('/')
            self.response.write(template.render({
                "greeting": 'Log Out',
                "url": logout_url,
            }))
        else:
            login_URL = users.create_login_url('/search')
            self.response.write(template.render({
                'greeting': 'Log In',
                "url": login_URL,
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
             datetime.date(2019, 9, 10))
        event = Event.query().filter(Event.event_name=="basketball game").get()
        # self.response.write("{} is the date and time".format(event.date_and_time))
        template = jinja_env.get_template('templates/eventpage.html')
        self.response.write(event)


class CategoryHandler(webapp2.RequestHandler):
    def get(self):
        categories = Category.query().order(Category.category_name).fetch()
        start_template = jinja_env.get_template("templates/eventpage.html")
        self.response.write(start_template.render({'category_info' : categories}))

class CalendarHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('/templates/calendar.html')
        self.response.write(template.render())

class SearchHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('/templates/home.html')
        self.response.write(template.render())


class EventPageHandler(webapp2.RequestHandler):
    def get(self):
        category = self.request.get("category")
        logging.info(category + "********")
        if category:
            events = Event.query().filter(Event.category==category).fetch()
        else:
            events = Event.query().fetch()
        template = jinja_env.get_template('/templates/eventpage.html')
        self.response.write(template.render({'events' : events}))
    def post(self):
        college_name = self.request.get("college_name")
        events = Event.query().filter(Event.college_name==college_name).fetch()
        template = jinja_env.get_template('/templates/eventpage.html')
        if events:
            self.response.write(template.render({'events':events}))
        else:
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
        time = map( int, self.request.get('time').split(":"))
        hour = time[0]
        minute = time[1]
        # addtional_info = self.request.get('additional_info')
        event_key = Event(event_name=event_name,
                organization_name=organization_name,
                college_name=college_name,
                category=category,
                location=location,
                date_and_time=datetime.date(year,month,day),
                time=datetime.time(hour, minute, 0, 0),
                # additional_info=additional_info
                ).put()

        # category = Category.query().filter(Category.category_name==category).get()
        # if not category.events:
        #     category.events = []
        # else:
        #     category.events.append(event_key)
        # category.put()

        self.response.write("<html><p>Your event: {} has been added, thank you.</p><a href='/addevent'>Back</a></html>".format(event_name))

class LoadDataHandler(webapp2.RequestHandler):
    def get(self):
        seed_data()
        # createEvent("basketball game", "gym", "basketball team", "Athletics", "Loyola Marymount University")


app = webapp2.WSGIApplication([
    ('/particles', particleHandler),
    ('/', SigninHandler),
    ('/search', SearchHandler),
    ('/calendar', CalendarHandler),
    ('/addevent', AddEventHandler),
    ('/events', EventPageHandler),
    ('/seed-data', LoadDataHandler),
    ('/categories', CategoryHandler),
], debug=True)
