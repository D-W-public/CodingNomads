import requests
from bs4 import BeautifulSoup

BASE_URL = "https://codingnomads.github.io/recipes/"

link_list = []

page = requests.get(BASE_URL)
soup = BeautifulSoup(page.text, features="html.parser")

links = soup.find_all("a")

for link in links:
    print(BASE_URL+link["href"])