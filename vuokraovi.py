# -*- coding: utf-8 -*-

import html
from optparse import OptionParser
import requests
import stringHandler
import urllib

if __name__ == '__main__':
	parser = OptionParser("usage: %prog [options] url saveloc")
	
	(opts, args) = parser.parse_args()
	if len(args) < 2:
		parser.error("url or save location missing")

	url = args[0]
	dirname = args[1]
	if not dirname.endswith('/'):
		dirname = dirname + '/'

	r = requests.get(url)
	htmlText = stringHandler.removeExcessNewlines(r.text)

	rawUrls = []
	imageParser = html.imageFinder(rawUrls)
	imageParser.feed(htmlText)

	imageUrls = stringHandler.pickImageUrls(rawUrls)

	imageIndex = 1
	for imageUrl in imageUrls:
		urllib.urlretrieve(imageUrl, stringHandler.generateFilename(imageUrl,
																dirname +
															 "testikuva" +
																'{:02d}'.format(imageIndex)))
		imageIndex += 1

	#asdf = stringHandler.removeParagraphTags(htmlText)
	#f = open('output.txt', 'w')
	#f.write(asdf.encode('utf8'))
	
	dataDict = {}
	tableParser = html.tableReader(dataDict)
	tableParser.feed(stringHandler.removeParagraphTags(htmlText))
#	for key in dataDict:
#		print(key + ": " + dataDict[key])

