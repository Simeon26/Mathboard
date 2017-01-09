import webapp2
import webapp2
import codecs
import os
import sys
import cgi
import urllib
import urllib2
from google.appengine.ext import db
from comment import DataString

class ViewPage(webapp2.RequestHandler):
    def get(self):
        room = (self.request.get("r"))#query for room
        key = db.Key.from_path('DataString', room)
        room_key = db.get(key)
        if room_key == None:
            #found not room - reroute to home page
            fullpath = os.path.join(os.path.split(__file__)[0], 'static_assets/html/index.html')
            page = codecs.open(fullpath, mode="r", encoding="utf-8")
            self.response.write(page.read())
        else:# join room
            fullpath = os.path.join(os.path.split(__file__)[0], 'static_assets/html/fabricreceiver.html')
            page = codecs.open(fullpath, mode="r", encoding="utf-8")
            self.response.write(page.read())

    def post(self):
        #update content of datastring object and increment its update counter
        room = self.request.get("room")
        updatecounter = self.request.get("updatecounter")
        key = db.Key.from_path('DataString', room)
        room = db.get(key)
        updatecounter = int(updatecounter.strip("'"))
        #updatecounter = int(updatecounter)
        if updatecounter == 1 or updatecounter < room.updatecounter:#cheeky way to return two values
            write = str(room.updatecounter) + "sometext like this sh3ould never a ctually apper so is a grt div%er" + room.content
            self.response.write(write)

app = webapp2.WSGIApplication([('/view', ViewPage),], debug=True)
