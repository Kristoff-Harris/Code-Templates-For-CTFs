# Some code reused fom freeCodeCamp() https://www.freecodecamp.org/news/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe/

import requests as req
import hashlib
from bs4 import BeautifulSoup

# specify the url
quote_page = req.get('http://docker.hackthebox.eu:32559')


# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(quote_page.text, 'html.parser')

# Take out the <div> of name and get its value
original_value = soup.find('h3')


value_to_hash = original_value.text.strip()
hashed_val = hashlib.md5(value_to_hash.encode())

print('Value to hash is : ' + str(value_to_hash))
print('Hashed Value is :' + str(hashed_val.hexdigest()))

post_data = {'hash': hashed_val}

post_req_response = req.post('http://docker.hackthebox.eu:32559', data=post_data )

print(post_req_response.text)
