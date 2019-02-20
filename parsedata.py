import json

with open('wikiData.json') as json_data:
  data = json.load(json_data)

for i in data:
    print (i['title'])