"""
You can watch a video of how to use DevTools in Chrome.
To download the Beautiful Soup 4 library:
pip install beautifulsoup4
To download the Requests library:
pip install requests
BeautifulSoup() analyzes the document.
The select() function returns all elements in the web page that match the given expression.
"""

import bs4
import requests

res = requests.get("https://jannatsari.com/")

# print(res.text)

noSearchSup = bs4.BeautifulSoup(res.text, 'html.parser')
print(type(noSearchSup))

element = noSearchSup.select("#description-container")

print(element)
print(element[0].getText())