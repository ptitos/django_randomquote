from django.http import HttpResponse
from django.template.loader import render_to_string
from urllib.parse import quote
import random, re, requests


def fetch_quotes(the_count):
	the_quotes = []
	max_quote_length = 300
	
	i = 0
	while i < the_count:
		the_num = random.randint(1,60000)
		the_url = 'https://www.quotes.net/quote/' + str(the_num)
		the_result = requests.get(the_url)
		if the_result.status_code == 200:
			the_match = re.search(r'<title>(.*)</title>', the_result.text)
			if (len(the_match.group(1)) <= max_quote_length):
				the_quotes.append(the_match.group(1))
				i += 1
	return the_quotes	

def index(request):
	all_texts = []
	all_authors = []
	all_quotes = []
	text_ids = []
	author_ids = []
	webified_text_ids = []
	webified_author_ids = []
	webified_quote_ids = []
	
	the_count = 11
	
	the_quotes = fetch_quotes(the_count)
	for i in range (1, the_count):
		text_ids.append('TEXT' + str(i));
		author_ids.append('AUTHOR' + str(i));
		webified_quote_ids.append('WEBIFIED_QUOTE' + str(i));

		the_parts = re.split(":", the_quotes[i], 1)	
		if len(the_parts) == 2:
			the_text = the_parts[1]
			the_author = the_parts[0]
		else:
			the_text = "Tempus fugit."
			the_author = "Unknown"

		all_texts.append(the_text)
		all_authors.append(the_author)
		temp_string = '"' + the_text + '":' + the_author
		all_quotes.append(temp_string)


	the_html = render_to_string('randomquote.html', {
		text_ids[0]: all_texts[0], 
		text_ids[1]: all_texts[1], 
		text_ids[2]: all_texts[2], 
		text_ids[3]: all_texts[3], 
		text_ids[4]: all_texts[4], 
		text_ids[5]: all_texts[5], 
		text_ids[6]: all_texts[6], 
		text_ids[7]: all_texts[7], 
		text_ids[8]: all_texts[8], 
		text_ids[9]: all_texts[9], 
		author_ids[0]: all_authors[0],
		author_ids[1]: all_authors[1],
		author_ids[2]: all_authors[2],
		author_ids[3]: all_authors[3],
		author_ids[4]: all_authors[4],
		author_ids[5]: all_authors[5],
		author_ids[6]: all_authors[6],
		author_ids[7]: all_authors[7],
		author_ids[8]: all_authors[8],
		author_ids[9]: all_authors[9],
		webified_quote_ids[0]: quote(all_quotes[0]), 
		webified_quote_ids[1]: quote(all_quotes[1]), 
		webified_quote_ids[2]: quote(all_quotes[2]), 
		webified_quote_ids[3]: quote(all_quotes[3]), 
		webified_quote_ids[4]: quote(all_quotes[4]), 
		webified_quote_ids[5]: quote(all_quotes[5]), 
		webified_quote_ids[6]: quote(all_quotes[6]), 
		webified_quote_ids[7]: quote(all_quotes[7]), 
		webified_quote_ids[8]: quote(all_quotes[8]), 
		webified_quote_ids[9]: quote(all_quotes[9]), 
		})

	return HttpResponse(the_html)
