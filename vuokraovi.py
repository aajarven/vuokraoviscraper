# -*- coding: utf-8 -*-

import html
import requests
import stringHandler
import urllib

#url = "https://www.vuokraovi.com/vuokra-asunto/helsinki/arabianranta/kerrostalo/547253"
url = "https://www.vuokraovi.com/vuokra-asunto/helsinki/kerrostalo/169310"
#url = "https://www.vuokraovi.com/vuokra-asunto/helsinki/arabianranta/kerrostalo/701979"
#url = "https://www.vuokraovi.com/vuokra-asunto/helsinki/kerrostalo/704590"
#headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0'}

r = requests.get(url)
htmlText = stringHandler.removeExcessNewlines(r.text)

raakakuvat = []
parser = html.imageFinder(raakakuvat)
parser.feed(htmlText)

kuvaurlit = stringHandler.pickImageUrls(raakakuvat)

kuvaindeksi = 1
for kuvaurl in kuvaurlit:
	urllib.urlretrieve(kuvaurl, stringHandler.generateFilename(kuvaurl,
															"testikuva" +
															'{:02d}'.format(kuvaindeksi)))
	kuvaindeksi += 1

f = open('output.txt', 'w')
#f.write(html.encode('utf8'))
