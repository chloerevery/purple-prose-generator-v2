import re

def strip(word):
	print("converted " + word)

	regex = re.compile('[^a-zA-Z]+') 
	regex.sub('', word) # TODO(Chloe): This code doesn't work
	word = word.lower()
	print(" to " + word)
	return word

def build_query(word):
	base_url = "http://words.bighugelabs.com/api"
	version = "2"
	api_key = "wouldn't you like to know" # TODO(Chloe): Factor this out into config
	data_format = "json"
	url = '{base_url}/{version}/{api_key}/{word}/{data_format}'.format(base_url=base_url, version=version, api_key=api_key, word=word, data_format=data_format)
	return url

def get_longest_syn(syn_list):
	longest_syn = ""
	for syn in syn_list: # For each value in map
		if len(syn) > len(longest_syn):
			longest_syn = syn
	return longest_syn