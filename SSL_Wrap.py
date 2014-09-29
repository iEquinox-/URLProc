import socket,ssl

class Wrap:
	def __init__(self, url):

		if not url.split(".")[0] == "www":
			self.url    = "www." + url
		else:
			self.url    = url

		self.exceptions = ["cloudflare.com"]
		self.socket     = socket.socket()
		self.ssl_file   = "sslkeys.pem"

	def Attempt(self):
		try:
			c = ssl.wrap_socket(
				self.socket,
				cert_reqs   = ssl.CERT_REQUIRED,
				ssl_version = ssl.PROTOCOL_SSLv3,
				ca_certs    = self.ssl_file
				)
			c.connect( ( self.url , 443 ) )
			certificate = c.getpeercert()
			commonName  = certificate['subject'][4][0][1]
			if commonName != self.url:
				if not ".".join(commonName.split(".")[1:]) in self.exceptions:
					return [False,"Unverified"]
				else:
					return [True,"Verified"]
			else:
				return [True,"Verified"]
		except Exception as e:
			print "Error parsed; " + str(e)
			quit()
