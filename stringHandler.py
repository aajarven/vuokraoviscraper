# -*- coding:utf-8 -*-

import re

class invalidUrlException(Exception):
	"""
	Exception reised when image url does not end in filename extension ('.'
	and up to five following characters)

	Attributes
	----------
	msg : string
		explanation of the Error
	"""

	def __init__(self, msg):
		self.expr = expr
		self.msg = msg


def removeExcessNewlines(text):
	"""
	Removes empty lines from text

	Attributes
	----------
	text : string
		text from which the empty lines are removed

	Returns
	-------
	string
		text without duplicated newlines
	"""
	return "\n".join([ll.rstrip() for ll in text.splitlines() if ll.strip()]) 

def pickImageUrls(strings):
	"""
	Picks image urls without '140x50,fit' (corresponding to the logo of the
	housing agency) in them, removes the image size string and replaces '//'
	with 'https://' to make a valid url

	Attributes
	----------
	strings : string array
		the urls from which full-size images are searched from

	Returns
	-------
	string array
		the urls
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

	Attributes
	----------
	url : string
		the url to which the extension is matched
	base : string
		base of the filename to which the extension is added

	Returns
	-------
	string
		the filename

	Raises
	------
	invalidUrlException
		when url does not contain a file extension
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

def cleanTableHeader(header):
	"""
	Removes whitespace and ':'

	Attributes
	----------
	header : string
		header to be cleaned

	Returns
	-------
	string
		cleaned header
	"""
	return re.sub(":", "", header.strip())

def concatData(original, added, separator):
	"""
	Concatenates additional string to original string, separated with a
	separator. If original string is empty, returns the additional string
	alone.

	Attributes
	----------
	original : string
		the original string (beginning of the new string)
	added : string
		the string to be added to the original string (end of the new string)
	separator : string
		the separator to be placed between the original and added strings
	"""
	if len(original) > 0:
		if len(added.strip()) > 0 and added.strip() != '\n':
			return original + separator + added.strip()
		else:
			return original
	else:
		if len(added.strip()) > 0 and added.strip() != '\n':
			return added.strip()
		else:
			return ""

def removeExcessSpaces(text):
	"""
	removes duplicate spaces, e.g. "stri      ng" -> "stri ng"
	
	Attributes
	----------
	text : string
		string from which duplicate spaces are removed

	Returns
	-------
	string
		same text without concurrent spaces
	"""

	return re.sub(" +", " ", text)

def removeAllNewlines(text):
	"""
	Removes all newlines from text and replaces them with spaces

	Attributes
	----------
	text : string
		string from which the newlines are removed
	
	Returns
	-------
	string
		the same string without newlines
	"""
	return re.sub("\n", " ", text)
