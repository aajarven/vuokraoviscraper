# -*- coding:utf-8 -*-

from HTMLParser import HTMLParser

class imageFinder(HTMLParser):

	def __init__(self, kuvat):
		self.kuvat = kuvat
		HTMLParser.__init__(self)
	
	def handle_startendtag(self, tag, attrs):
		if tag == "img":
			for a in attrs:
				if a[0] == "src" or a[0] == "data-cycle-src":
					if ("_original") in a[1]:
						self.kuvat.append(a[1])
