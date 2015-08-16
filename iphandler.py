from google.appengine.ext import ndb

import webapp2

class IP(ndb.Model):
    address = ndb.StringProperty()
    updated = ndb.DateTimeProperty(auto_now_add=True)

class IPHandler(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(IP.query().order(-IP.updated).fetch(1)[0].address)
    def post(self):
        ip = self.request.body
        IP(address = ip).put()

app = webapp2.WSGIApplication([
    (r'/', IPHandler),
    (r'/update', IPHandler)
])