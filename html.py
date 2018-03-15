# -*- coding:utf-8 -*-

from HTMLParser import HTMLParser
import stringHandler

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
		self.inTd = False
		self.inTh = False
		self.lastKey = ""
		HTMLParser.__init__(self)

	def handle_starttag(self, tag, attrs):
		if tag == "tbody":
			self.inTbody = True
		elif self.inTbody and tag == "tr":
			self.inTr = True
		elif tag == "td":
			self.inTd = True
		elif tag == "th":
			self.inTh = True

	def handle_endtag(self, tag):
		if tag == "tbody":
			self.inTbody = False
		if tag == "tr":
			self.inTr = False
		if tag == "td":
			self.inTd = False
		if tag == "th":
			self.inTh = False
	
	def handle_data(self, data):
		# description
		if self.inTbody and not self.inTr:
			if "description" in self.dataDict:
				descr = self.dataDict["description"]
			else:
				descr = ""

			self.dataDict["description"] = stringHandler.concatData(descr,
														   data, "\n")

		# other fields
		if self.inTh:
			self.lastKey = stringHandler.cleanTableHeader(data)
		elif self.inTd and len(self.lastKey) > 0:
			if self.lastKey in self.dataDict:
				originalData = self.dataDict[self.lastKey]
			else:
				originalData = ""

			cleanedData = stringHandler.concatData(originalData, data,
											   " ")
			cleanedData = stringHandler.removeAllNewlines(cleanedData)
			cleanedData = stringHandler.removeExcessSpaces(cleanedData)
			self.dataDict[self.lastKey] = cleanedData
