import json
import requests
from bs4 import BeautifulSoup
from pprint import pprint

BASE_URL = "https://codingnomads.github.io/recipes/"

link_list = []

page = requests.get(BASE_URL)
soup = BeautifulSoup(page.text, features="html.parser")

links = soup.find_all("a")

for link in links:
    link = (BASE_URL+link["href"])
    link_list.append(link)

with open("list_of_links.txt", "w") as f:
    for item in link_list:
        f.write(str(item) +"\n")