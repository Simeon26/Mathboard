import webapp2
import codecs
import os


class MainPage(webapp2.RequestHandler):
    def get(self):
        #simply loads the home page
        fullpath = os.path.join(os.path.split(__file__)[0], 'static_assets/html/index.html')
        page = codecs.open(fullpath, mode="r", encoding="utf-8")
        self.response.write(page.read())

app = webapp2.WSGIApplication([('/', MainPage),], debug=True)
