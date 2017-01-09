import webapp2
import codecs
import os
import sys
import cgi
import urllib
import urllib2
import random
from google.appengine.ext import db
from comment import DataString
'''

class DataString(db.Model):
    content =db.TextProperty()
    roomnumber =db.StringProperty()
    updatecounter =db.IntegerProperty()
    comments =db.TextProperty()
'''

class DrawPage(webapp2.RequestHandler):
    def get(self):
        room = (self.request.get("r"))
        key = db.Key.from_path('DataString', room)
        room_key = db.get(key)
        if room_key != None:
            #failed to find room
            fullpath = os.path.join(os.path.split(__file__)[0], 'static_assets/html/index.html')
            page = codecs.open(fullpath, mode="r", encoding="utf-8")
            self.response.write("<script type='text/javascript'>window.location= '/'</script>")
        else:
            #make new datastring object 
            datastring = DataString(key_name = room)
            datastring.roomnumber = room
            datastring.content = "none"
            datastring.updatecounter = 1
            datastring.comments = "<div class='comment'>Welcome to room " + room + "</div>" # innital comment
            datastring.put() #this adds it to the gae datastore
            fullpath = os.path.join(os.path.split(__file__)[0], 'static_assets/html/fabrictest.htm')#load correct page
            page = codecs.open(fullpath, mode="r", encoding="utf-8")
            self.response.write(page.read())
        
    def post(self):
        room = self.request.get("room")
        key = db.Key.from_path('DataString', room)
        room = db.get(key)#result of query
        room.content = self.request.get("data")#update data content
        room.updatecounter = room.updatecounter + 1
        room.put()

app = webapp2.WSGIApplication([('/draw', DrawPage),], debug=True)
