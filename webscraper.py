from bs4 import BeautifulSoup
import requests
import re

url = 'https://en.wikipedia.org/wiki/RMS_Titanic'
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, 'html.parser')
text = content.find('div', attrs={"class": "mw-parser-output"})
links = []

for link in text.findAll('a', attrs={'href': re.compile("^/wiki/")}):
  if link not in links:
    links.append({
      "title": link.text,
      "url": link['href']
    })

print(links[0:5])