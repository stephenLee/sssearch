import os

import webapp2

import jinja2

jinja_environment=jinja2.Environment(autoescape=True,
        loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')))

class HomeHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {}

        template = jinja_environment.get_template('base.html')
        self.response.out.write(template.render(template_values))

app = webapp2.WSGIApplication([('/',HomeHandler)], debug=True)
