# -*- coding: utf-8 -*-

import re
import requests
from HTMLParser import HTMLParser
import urllib

class MyHTMLParser(HTMLParser):

	def __init__(self, kuvat):
		self.kuvat = kuvat
		HTMLParser.__init__(self)
	
	def handle_startendtag(self, tag, attrs):
		if tag == "img":
			for a in attrs:
				if a[0] == "src" or a[0] == "data-cycle-src":
					if ("_original") in a[1]:
						self.kuvat.append(a[1])


#url = "https://www.vuokraovi.com/vuokra-asunto/helsinki/arabianranta/kerrostalo/547253"
url = "https://www.vuokraovi.com/vuokra-asunto/helsinki/kerrostalo/169310"
#url = "https://www.vuokraovi.com/vuokra-asunto/helsinki/arabianranta/kerrostalo/701979"
#url = "https://www.vuokraovi.com/vuokra-asunto/helsinki/kerrostalo/704590"
#headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0'}

r = requests.get(url)

raakakuvat = []
parser = MyHTMLParser(raakakuvat)

html = "\n".join([ll.rstrip() for ll in r.text.splitlines() if ll.strip()]) 

parser.feed(html)
kuvaurlit = []
for kuva in raakakuvat:
	if "140x50,fit" not in kuva:
		k = re.sub(r"\d+x\d+,fit/", "", kuva)
		kuvaurlit.append(k.replace("//", "https://", 1))

kuvaindeksi = 1
for kuvaurl in kuvaurlit:
	urllib.urlretrieve(kuvaurl, "testikuva"+str(kuvaindeksi))
	kuvaindeksi += 1

f = open('output.txt', 'w')
f.write(html.encode('utf8'))
