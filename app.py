import time, requests, helpers

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# requests_cache.install_cache('github_cache', backend='sqlite', expire_after=180)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
    	to_translate = request.form['prose']

    	word_list = to_translate.split(" ") # Split toTranslate on spaces
    	purplified_prose = "" # Create purplifiedProse string
        
        # Create map with key [original word in toTranslate], value [lowercase, non-punctuated equivalent]
        word_map = {}
        for word in word_list:
        	word_map[word] = helpers.strip(word)
        
        for word in word_map.values(): # For each value in map
        		# StringToAppendToPurplifiedProse <-- value
        		# Result = result of call to thesaurus api
	        		# For now, assume all words are nouns if thesaurus api returns an array of noun synonyms
	        		# Later: integrate sentence parsing API to determine likely part of speech of each word
        		# If result.nouns != null
        			# Iterate through result, return longest synonym
        			# (Stretch) use map to mimic original punctuation and case
        			# StringToAppendToPurplifiedProse --> longest synonym
        		# Append StringToAppendToPurplifiedProse to purplifiedProse
        # Send purplifiedProse into 'results' div

        url = "http://words.bighugelabs.com/api/2/0b4bb7369d73af737d44f66e89f66c99/" + to_translate + "/json"
        
        response = requests.get(url)
        results = jsonify(response.json())

       	return render_template('index.html', results=results)

    return render_template('index.html')

       
    #     return jsonify(response.json())
	


if __name__ == '__main__':
    app.run(debug=True)

    

