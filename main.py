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

class EventPageHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('templates/main.html')
        self.response.write(template.render())

class CalendarHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('templates/main.html')
        self.response.write(template.render())

class SearchHandler(webapp2.RequestHandler):
    def post(self):
        filter = self.request.get('filter')
        base_url = 'https://ghibliapi.herokuapp.com/{}'.format(filter)
        response = json.loads(urlfetch.fetch(base_url).content)
        template = jinja_env.get_template('templates/results.html')
        self.response.write(template.render({ 'response': response }))

        # params = {
        #     'q': self.request.get('query'),
        #     'i': self.request.get('ingredients')}
        # response = json.loads(urlfetch.fetch(base_url + urlencode(params)).content)
class SigninHandler(webapp2.RequestHandler):
    def post(self):
        filter = self.request.get('filter')
        base_url = 'https://ghibliapi.herokuapp.com/{}'.format(filter)
        response = json.loads(urlfetch.fetch(base_url).content)
        template = jinja_env.get_template('templates/results.html')
        self.response.write(template.render({ 'response': response }))

class AddEventHandler(webapp2.RequestHandler):
    def post(self):
        filter = self.request.get('filter')
        base_url = 'https://ghibliapi.herokuapp.com/{}'.format(filter)
        response = json.loads(urlfetch.fetch(base_url).content)
        template = jinja_env.get_template('templates/results.html')
        self.response.write(template.render({ 'response': response }))


app = webapp2.WSGIApplication([
    ('/', MainPageHandler),
    ('/search', SearchHandler),
], debug=True)
