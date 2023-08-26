import requests
from bs4 import BeautifulSoup

url = "https://codingnomads.github.io/recipes/recipes/9-authentic-german-che.html"

page = requests.get(url)
soup = BeautifulSoup(page.text, features="html.parser")

title = soup.find("h1", class_="title")
author = soup.find("p", class_="author")
recipe = soup.find("div", class_="md")

print(title.text)
print(author.text.strip("by "))
print(recipe.text)