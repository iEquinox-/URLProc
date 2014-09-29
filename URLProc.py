import urllib,urllib2,json,cookielib

class URLProc:
	def __init__(self,url,protocol,queue):
		self.comprehension = dict()
		self.url           = url
		self.protocol      = protocol
		self.headers       = dict()
		self.cookies       = dict()
		self.cookie_handle = cookielib.LWPCookieJar()
		self.hanlders      = [urllib2.HTTPHandler(), urllib2.HTTPSHandler(), urllib2.HTTPCookieProcessor(self.cookie_handle)]
		self.management    = urllib2.build_opener(*self.hanlders)
		self.queue         = queue

	def Retrieve(self,url,protocol,type):
		if type == 0:
			if protocol == 0: request = urllib2.Request("http://%s"%(url))
			if protocol == 1: request = urllib2.Request("https://%s"%(url))

			self.management.open(request)
			for cookie in self.cookie_handle:
				self.cookies[cookie.name] = json.dumps(cookie.value)
			return self.cookies
		if type == 1:
			if protocol == 0: request = "http://%s"%(url)
			if protocol == 1: request = "https://%s"%(url)

			for header,value in urllib2.urlopen(request).headers.items():
				self.headers[header] = json.dumps(value)
			return self.headers

	def Feed(self):
		if(self.queue != None)and(len(self.queue)>0):
			for url in self.queue:
				tmp = {"protocol":url[1], "cookies":self.Retrieve(url[0],url[1],0), "headers":self.Retrieve(url[0],url[1],1) }
				self.comprehension[url[0]] = tmp
		else:
			tmp = {"protocol":self.protocol, "cookies":self.Retrieve(self.url,self.protocol,0), "headers":self.Retrieve(self.url,self.protocol,1)}
			self.comprehension[self.url] = tmp
		return self.comprehension
