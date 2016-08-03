import time, requests, helpers

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# requests_cache.install_cache('github_cache', backend='sqlite', expire_after=180)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
    	to_translate = request.form['prose']

    	word_list = to_translate.split(" ") # Split toTranslate on spaces
        
        # Create map with key [original word in toTranslate], value [lowercase, non-punctuated equivalent]
        word_map = {} # TODO(Chloe): Handle case where sentence contains same word twice, in different contexts
        for word in word_list:
        	word_map[word] = helpers.strip(word)
        
        for word in word_map.values(): # For each value in map
        		curr_word = word # StringToAppendToPurplifiedProse <-- value
        		# Resp = result of call to thesaurus api
        		url = helpers.build_query(word) 
        		print(url)
        		try: 
        			resp = requests.get(url) # TODO(Chloe): Add error handling
        		except requests.exceptions.RequestException as e:    # This is the correct syntax
        			print e
        		if resp.status_code != 200:
        			word_map[word] = word
        			break
				    
	        	# For now, assume all words are nouns if thesaurus api returns an array of noun synonyms
	        	# Later: integrate sentence parsing API to determine likely part of speech of each word
	        	longest_syn = ""
	        	if 'noun' in resp.json().keys():
	        		if 'syn' in resp.json()['noun'].keys():
	        			longest_syn = helpers.get_longest_syn(resp.json()['noun']['syn'])

        		longest_syn = longest_syn if len(longest_syn) > len(word) else word
        		print("longest syn: " + longest_syn)

        		# add longest syn to map
        		word_map[word] = longest_syn

        		# TODO(Chloe): Use map to mimic original punctuation and case

        purplified_prose = ""
        print(word_map)
        for word in word_list:
        	purplified_prose += word_map[word] + " "


        		
        # Send purplifiedProse into 'results' div


        
        

       	return render_template('index.html', results=purplified_prose)

    return render_template('index.html')

       
    #     return jsonify(response.json())
	


if __name__ == '__main__':
    app.run(debug=True)

    

