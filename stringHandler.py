# -*- coding:utf-8 -*-

import re

class invalidUrlException(Exception):
	"""
	Exception reised when image url does not end in filename extension ('.'
	and up to five following characters)

	Attributes:
		msg  -- explanation of the Error
	"""

	def __init__(self, msg):
		self.expr = expr
		self.msg = msg


def removeExcessNewlines(text):
	"""
	Removes empty lines from text

	Attributes:
		text -- text from which the empty lines are removed
	"""
	return "\n".join([ll.rstrip() for ll in text.splitlines() if ll.strip()]) 

def pickImageUrls(strings):
	"""
	Picks image urls without '140x50,fit' (corresponding to the logo of the
	housing agency) in them, removes the image size string and replaces '//'
	with 'https://' to make a valid url

	Attributes:
		strings -- the urls from which full-size images are searched from
	"""
	kuvaurlit = []
	for url in strings:
		if "140x50,fit" not in url:
			k = re.sub(r"\d+x\d+,fit/", "", url)
			kuvaurlit.append(k.replace("//", "https://", 1))
	return kuvaurlit

def generateFilename(url, base):
	""" 
	Generates filename for the image from given url using the given base and
	the same extension as in the url

	Attributes:
		url  -- the url to which the extension is matched
		base -- base of the filename to which the extension is added
	
	Raises:
		invalidUrlException -- when url does not contain a file extension
	"""

	for i in range(1, 5):
		if url[-1*i] == '.':
			return base + url[-1*i:]

	# raise error if no extension found
	raise invalidUrlException("Invalid url, no extension found: " + url)

def removeParagraphTags(text):
	"""
	Removes <p> tags and replaces each sequence whitespace-separated <p> tags
	with a single newline

	Attributes
	----------
	text : string
		Text in which the <p> tags are to be replaced

	Returns
	-------
	string
		A string where <p> tags have been replaced with newlines
	"""
	return re.sub("(<p>\s*)+", "\n", text)
