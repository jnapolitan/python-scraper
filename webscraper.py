from bs4 import BeautifulSoup
import requests
import re
import json

url = 'https://en.wikipedia.org/wiki/Python_(programming_language)'
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, 'html.parser')
text = content.find('div', attrs={"class": "mw-parser-output"})
links = []

for link in text.findAll('a', attrs={'href': re.compile("^/wiki/")}):
  if link.text and link not in links:
    links.append({
      "title": link['title'],
      "url": link['href']
    }) 
    
with open('wikiData.json', 'w') as outfile:
  json.dump(links[0:5], outfile)