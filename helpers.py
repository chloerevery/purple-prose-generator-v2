import re

def strip(word):
	regex = re.compile('[^a-zA-Z]')
	regex.sub('', word)
	word = word.lower()

	return word