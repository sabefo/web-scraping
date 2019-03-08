from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from html2json import collect
from googlesearch import search

query = "carta el tenedor tako daruma madrid"

hdr = { 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive' }

for j in search(query, tld = "co.in", num = 10, stop = 1, pause = 2):
	print(j)
	html = Request(j, headers = hdr)
	html = urlopen(html)

	res = BeautifulSoup(html.read(), "lxml");
	for x in res.find('div', { 'class': 'restaurantTabContent' }):
		li = x.find_all('li')
		for l in li:
			print(l.get_text())
			print('----------------')

# mydivs = soup.findAll("div", {"class": "stylelistrow"})
# try:
#     page = urllib2.urlopen(req)
# except urllib2.HTTPError, e:
#     print e.fp.read()

# content = page.read()
# print content