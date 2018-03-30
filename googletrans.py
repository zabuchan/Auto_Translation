import sys
import json
import requests

def do_translation(input_text, key):
	sys.stdout.write('English: {}'.format(input_text))
	

	url = "https://translation.googleapis.com/language/translate/v2"
	url += "?key=" + key
	url += "&q=" + input_text
	url += "&source=en&target=ja"

	response = requests.get(url)
	unit_aa=json.loads(response.text)
	translated_text = unit_aa["data"]["translations"][0]["translatedText"]
	sys.stdout.write('日本語: {}'.format(translated_text))
	# Return Key
	print('')
	print('')


def read_api_key(filename):
	try:
		with open(filename, 'r') as f:
				api_key = f.readline()
				return api_key
	except EnvironmentError:
  		raise('No file was found.')

def read_source(src, key):
	try:
		with open(src) as f:
			for line in f:
				#sys.stdout.write(line)
			  do_translation(line, key)
	except EnvironmentError:
  		raise('No file was found.')

api_key = read_api_key('Google_Translation_API_KEY')
read_source('steve_jobs_starnford_speech.txt', api_key)