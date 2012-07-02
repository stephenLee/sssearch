import os
import random
from string import letters

import webapp2
from webapp2_extras import sessions
import jinja2

jinja_environment=jinja2.Environment(autoescape=True,
        loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')))

class BaseHandler(webapp2.RequestHandler):
    def dispatch(self):
        #Get a session store for this request
        self.session_store = sessions.get_store(request=self.request)
        
        try:
            #Dispatch the request
            webapp2.RequestHandler.dispatch(self)
        finally:
            #save all sessions
            self.session_store.save_sessions(self.response)
            
    @webapp2.cached_property
    def session(self):
        # Returns a session using the default cookie key
        return self.session_store.get_session()

class HomeHandler(BaseHandler):
    def get(self):
        self.session['foo'] = 'bar'
        foo = self.session.get('foo')
        template_values = {
            'name': 'Stephen',
            'verb': 'extremely enjoy',
            'session': foo
            }

        template = jinja_environment.get_template('index.html')
        self.response.out.write(template.render(template_values))

def make_secret_key(length=10):
    return ''.join(random.choice(letters) for unused in xrange(length))

secret_key = make_secret_key()

config = {}
config['webapp2_extras.sessions'] = {
    'secret_key': secret_key
}

app = webapp2.WSGIApplication([('/',HomeHandler)],config=config, debug=True)
