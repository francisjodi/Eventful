import os
import json
import webapp2
import jinja2
from urllib import urlencode
from google.appengine.api import urlfetch

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

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
        template = jinja_env.get_template('templates/eventpage.html')
        self.response.write(template.render())

class CalendarHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('templates/calendar.html')
        self.response.write(template.render())

class SearchHandler(webapp2.RequestHandler):
    def post(self):
        filter = self.request.get('filter')
        template = jinja_env.get_template('templates/home.html')
        self.response.write(template.render({ 'response': response }))



class AddEventHandler(webapp2.RequestHandler):
    def post(self):
        filter = self.request.get('filter')
        template = jinja_env.get_template('templates/addevent.html')
        self.response.write(template.render({ 'response': response }))


app = webapp2.WSGIApplication([
    ('/', SigninHandler),
    ('/search', SearchHandler),
    ('/calendar', CalendarHandler),
    ('/addevent', AddEventHandler),
    ('/events', EventPageHandler),
], debug=True)
