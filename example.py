import URLProc

#### Get a specific website's cookies & headers

example1 = URLProc.URLProc(url="sinister.ly",protocol=1,queue=None).Feed()

#### => {'headers': {'x-powered-by': '"PHP/5.3.29-1~dotdeb.0"', 'transfer-encoding': '"chunked"', 'set-cookie': '"__cfduid=d774c3d8afec26930be83331a680a4c931411972239432; expires=Mon, 23-Dec-2019 23:50:00 GMT; path=/; domain=.sinister.ly; HttpOnly, mybb[lastvisit]=1411972230; expires=Tue, 29-Sep-2015 06:30:30 GMT; path=/; domain=.sinister.ly, mybb[lastactive]=1411972230; expires=Tue, 29-Sep-2015 06:30:30 GMT; path=/; domain=.sinister.ly, sid=98fd1ea5aa6453e436ec4d7070dddccc; path=/; domain=.sinister.ly; HttpOnly"', 'strict-transport-security': '"max-age=31536000"', 'mobiquo_is_login': '"false"', 'server': '"cloudflare-nginx"', 'connection': '"close"', 'date': '"Mon, 29 Sep 2014 06:30:39 GMT"', 'cf-ray': '"17162220785b0950-DFW"', 'content-type': '"text/html; charset=UTF-8"'}, 'cookies': {'mybb[lastvisit]': '"1411972229"', 'sid': '"0a2c63ccc7109f5baf157336eb8a200d"', 'mybb[lastactive]': '"1411972229"', '__cfduid': '"d2096d4bc4325170a5e0564bd5f2bc8081411972238313"'}, 'protocol': 1}
#### Protocol uses only HTTP and HTTPS
#### 0 = HTTP
#### 1 = HTTPS

#### Queue used to grab data from multiple websites; in this case queue is None, since we do not want to grab data from multiple websites.
#### Using queue;

example2 = URLProc.URLProc(url="",protocol=0,queue=[ ["sinister.ly",1], ["127.0.0.1",0] ]).Feed()

#### Queue is a list of sites and their protocols ([site,protocol]).
#### Because Feed() returns the data as a dictionary, you can easily find specific data from a website.

print example2["127.0.0.1"] # => Returns localhost's data.
print example2["127.0.0.1"]["cookies"] # => Returns localhost's cookies (if any. In most cases, localhost will not have any cookies set/ to set).
print example2["127.0.0.1"]["headers"] # => Returns localhost's headers.

#### All data is contained in a dictionary, meaning you can find all data that you would like.

print example2["127.0.0.1"]["headers"]["server"] # => Returns the server; to get the string format without quotes around the string, use JSON.

import json

print json.loads( example2["127.0.0.1"]["headers"]["server"] )
