import urllib,urllib2,json,cookielib,time

import SSL_Wrap

class URLProc:
	def __init__(self,url,protocol):
		self.comprehension = dict()
		self.url           = url
		self.protocol      = protocol
		self.headers       = dict()
		self.cookie_handle = cookielib.LWPCookieJar()
		self.hanlders      = [urllib2.HTTPHandler(), urllib2.HTTPSHandler(), urllib2.HTTPCookieProcessor(self.cookie_handle)]
		self.management    = urllib2.build_opener(*self.hanlders)
		self.ssl           = dict()
		self.cookies       = dict()

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
		if type == 2:
			if protocol == 0:
				self.ssl["SSL"] = False
			if protocol == 1:
				wrapped = SSL_Wrap.Wrap(url=url).Attempt()
				if wrapped[0] == True:
					self.ssl["SSL"] = json.dumps(wrapped[1])
				else:
					self.ssl["SSL"] = json.dumps(wrapped[0])
			return self.ssl

	def Feed(self):
		tmp = {"protocol":self.protocol, "cookies":self.Retrieve(self.url,self.protocol,0), "headers":self.Retrieve(self.url,self.protocol,1), "ssl":self.Retrieve(self.url,self.protocol,2)}
		return tmp
