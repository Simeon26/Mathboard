import webapp2
import wolframalpha

class WolfPage(webapp2.RequestHandler):        
	def post(self):
		#grabs input equation from wolframalpha bar at bottom of page
		tPostVariable = self.request.get('equation')
		#setup client object with wolfram api key
		client = wolframalpha.Client('4XUQL2-GYULW3729X')
		
		res = client.query(tPostVariable)
		#loop through all responses from wolfram api, display relevant images on page
		for pod in res.pods:
			for sub in pod.subpods:
				for img in sub.img:
					if pod.id == 'Result' or pod.id == 'Plot':
						self.response.write(img.src)

app = webapp2.WSGIApplication([('/wolf', WolfPage),], debug=True)
