
import json
import requests
from pprint import pprint
"""
url = "https://ghibliapi-iansedano.vercel.app/api/films"

response = requests.get(url)

data = response.json()

with open("films.json", "w") as fout:
    json.dump(data, fout)
"""

with open("films.json", "r") as fin:
    data = json.load(fin)


pprint(data)