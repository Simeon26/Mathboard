import webapp2
import codecs
import os

class ErrorPage(webapp2.RequestHandler):
    def get(self):
        #Simply displays a html page
        fullpath = os.path.join(os.path.split(__file__)[0], 'static_assets/html/404.html')
        page = codecs.open(fullpath, mode="r", encoding="utf-8")
        self.response.write(page.read())

app = webapp2.WSGIApplication([('/.*', ErrorPage),], debug=True)
