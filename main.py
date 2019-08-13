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
# from googleapiclient.discovery import build
# from google_auth_oauthlib.flow import InstalledAppFlow
# from google.auth.transport.requests import Request

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

        # # The file token.pickle stores the user's access and refresh tokens, and is
        # # created automatically when the authorization flow completes for the first
        # # time.
        # if os.path.exists('token.pickle'):
        #     with open('token.pickle', 'rb') as token:
        #         creds = pickle.load(token)
        # # If there are no (valid) credentials available, let the user log in.
        # if not creds or not creds.valid:
        #     if creds and creds.expired and creds.refresh_token:
        #         creds.refresh(Request())
        #     else:
        #         flow = InstalledAppFlow.from_client_secrets_file(
        #             'credentials.json', SCOPES)
        #         creds = flow.run_local_server(port=0)
        #     # Save the credentials for the next run
        #     with open('token.pickle', 'wb') as token:
        #         pickle.dump(creds, token)

        # service = build('calendar', 'v3', credentials=creds)

        # # Call the Calendar API
        # now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
        # print('Getting the upcoming 10 events')
        # events_result = service.events().list(calendarId='primary', timeMin=now,
        #                                     maxResults=10, singleEvents=True,
        #                                     orderBy='startTime').execute()
        # events = events_result.get('items', [])
    
        # if not events:
        #     print('No upcoming events found.')
        # for event in events:
        #     start = event['start'].get('dateTime', event['start'].get('date'))
        #     print(start, event['summary'])
        

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
        category = self.request.get("category")
        if category:
            events = Event.query().filter(Event.category==category).fetch()
        else:
            events = Event.query().fetch()
        template = jinja_env.get_template('/templates/eventpage.html')
        self.response.write(template.render({'events' : events}))

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

        category = Category.query().filter(Category.category_name==category).get()
        if not category.events:
            category.events = []
        else:
            category.events.append(event_key)
        category.put()


        self.response.write("Your event: {} has been added, thank you.".format(event_name))

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
    ('/categories', CategoryHandler),
], debug=True)
