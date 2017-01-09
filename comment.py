import webapp2
from google.appengine.ext import db

class DataString(db.Model):
    content =db.TextProperty()
    roomnumber =db.StringProperty()
    updatecounter =db.IntegerProperty()
    comments =db.TextProperty()

class Comment(webapp2.RequestHandler):
    def get(self):
        #queries datastore for datastring object and writes the content of its commentes
        room = self.request.get("r")
        key = db.Key.from_path('DataString', room)
        room = db.get(key)
        write = room.comments
        self.response.write(write)
        
    def post(self):
        #queries datastore for datastring object adds comment ajax argument to the comments string and updates the datastring object
        room = self.request.get("room")
        key = db.Key.from_path('DataString', room)
        room = db.get(key)
        com = room.comments
        #print com
        room.comments = com + self.request.get("comment")
        #print room.comments
        room.put()

app = webapp2.WSGIApplication([('/comment', Comment),], debug=True)
