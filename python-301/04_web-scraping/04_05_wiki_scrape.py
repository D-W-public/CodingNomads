# Write a web scraper that fetches the information from the Wikipedia page
# on Web scraping. Extract all the links on the page and filter them so the
# navigation links are excluded.
# Programmatically follow one of the links that lead to another Wikipedia article,
# extract the text content from that article, and save it to a local text file.
# BONUS TASK: Use RegExp to find all numbers in the text.
import requests
from bs4 import BeautifulSoup
from pprint import pprint
import re

url = "https://en.wikipedia.org/wiki/Web_scraping"

response = requests.get(url)
content = response.content

soup = BeautifulSoup(content, features="html.parser")

links = soup.find_all("a")
url_set = set()
excluded_prefixes = ("Main_Page", "Portal:", "Help:","Talk:", "Special:", "File:","Wikipedia:", "Category:")

for link in links:
    href = link.get("href")
    if href and href.startswith("/wiki/")and not any(href.startswith("/wiki/"+ prefix) for prefix in excluded_prefixes):
        url_set.add("https://en.wikipedia.org" + href)


url_list = list(url_set)

url_2 = url_list[9]

page = requests.get(url_2)
soup = BeautifulSoup(page.text, features="html.parser")

content = soup.find("div", class_="mw-parser-output")

pprint(content.text)

with open("link_10.txt", "w",encoding="utf-8") as f:
    f.write(content.text)

with open("link_10.txt", "r") as file:
    content = file.read()

pattern = r'\b\d+\b'

matches = re.findall(pattern, content)

for match in matches:
    print(match)