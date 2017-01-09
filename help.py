import webapp2
import codecs
import os
import sys

class HelpPage(webapp2.RequestHandler):
    def get(self):
        #simply loads a html file
        fullpath = os.path.join(os.path.split(__file__)[0], 'static_assets/html/help.html')
        page = codecs.open(fullpath, mode="r", encoding="utf-8")
        self.response.write(page.read())

app = webapp2.WSGIApplication([('/help', HelpPage),], debug=True)
