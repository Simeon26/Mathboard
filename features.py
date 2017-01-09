import webapp2
import codecs
import os
import sys

class FeaturesPage(webapp2.RequestHandler):
    def get(self):
        #simply loads a html page
        fullpath = os.path.join(os.path.split(__file__)[0], 'static_assets/html/features.html')
        page = codecs.open(fullpath, mode="r", encoding="utf-8")
        self.response.write(page.read())

app = webapp2.WSGIApplication([('/features', FeaturesPage),], debug=True)
