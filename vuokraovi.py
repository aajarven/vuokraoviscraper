# -*- coding: utf-8 -*-

import html
from optparse import OptionParser
import os
import re
import requests
import stringHandler
import urllib

if __name__ == '__main__':
	parser = OptionParser("usage: %prog [options] url saveloc")
	parser.add_option("-d", "--outputdir", dest="outputdir",
				   help=("A directory in which the apartment directories",
			 "will be created"), default="apartments/")
	
	(opts, args) = parser.parse_args()
	if len(args) < 1:
		parser.error("url missing")

	url = args[0]
	dirname = opts.outputdir
	if not dirname.endswith('/'):
		dirname = dirname + '/'

	# html
	r = requests.get(url)
	htmlText = stringHandler.removeExcessNewlines(r.text)

	# apartment data
	dataDict = {}
	tableParser = html.tableReader(dataDict)
	tableParser.feed(stringHandler.removeParagraphTags(htmlText))

	# directory for saving
	fullDirname = dirname + dataDict['Kohdenumero'] + "-" +	dataDict['Kuvaus'] + "-" + re.findall(r"\d+",
									   dataDict['Asuinpinta-ala'])[0] + "/"
	if not os.path.exists(fullDirname):
		os.makedirs(fullDirname)

	# write apartment information
	f = open(fullDirname + "info.txt", 'w')
	f.write(dataDict['description'].encode('utf8'))
	f.write("\n")
	for key in dataDict:
		if key != 'description':
			line = key + ": " + dataDict[key]
			f.write("\n")
			f.write(line.encode('utf-8'))
	f.close()

	# images
	rawUrls = []
	imageParser = html.imageFinder(rawUrls)
	imageParser.feed(htmlText)
	imageUrls = stringHandler.pickImageUrls(rawUrls)

	imageIndex = 1
	for imageUrl in imageUrls:
		urllib.urlretrieve(imageUrl,
					 stringHandler.generateFilename(imageUrl, fullDirname + "kuva"
									 + '{:02d}'.format(imageIndex)))
		imageIndex += 1
