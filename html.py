# -*- coding:utf-8 -*-

from HTMLParser import HTMLParser

class imageFinder(HTMLParser):

	def __init__(self, images):
		self.images = images
		HTMLParser.__init__(self)
	
	def handle_startendtag(self, tag, attrs):
		if tag == "img":
			for a in attrs:
				if a[0] == "src" or a[0] == "data-cycle-src":
					if ("_original") in a[1]:
						self.images.append(a[1])


class tableReader(HTMLParser):

	def __init__(self, dataDict):
		self.dataDict = dataDict
		self.inTbody = False
		self.inTr = False
		HTMLParser.__init__(self)

	def handle_starttag(self, tag, attrs):
		if tag == 'tbody':
			self.inTbody = True
		elif self.inTbody and tag == 'tr':
			self.inTr = True

	def handle_endtag(self, tag):
		if tag == 'tbody':
			self.inTbody = False
		if tag == 'tr':
			self.inTr = False
	
	def handle_data(self, data):
		if self.inTbody and not self.inTr:
			if 'description' in self.dataDict:
				descr = self.dataDict['description']
				if len(data.strip()) > 0 and data.strip() != '\n':
					descr = descr + "\n" + data.strip()
			else:
				if len(data.strip()) > 0 and data.strip() != '\n':
					descr =  data.strip()
				else:
					descr = ""

			self.dataDict['description'] = descr

