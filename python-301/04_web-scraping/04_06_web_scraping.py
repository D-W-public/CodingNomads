# Look for a static website online that has some information that you're
# interested in. Follow the web-scraping steps described in the course to
# inspect, scrape, and parse the information.
# BE RESPECTFUL! Don't scrape sites that don't want to be scraped, and
# limit the amount of calls you make to their page by saving the response
# to a file, and parsing the content from that file.

import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json

# url = "https://starwars.fandom.com/wiki/Jedi_Order"

# page = requests.get(url)
# soup = BeautifulSoup(page.text, features="html.parser")

# title = soup.find("div", class_="page-header__title-wrapper")
# article = soup.find("div", class_="mw-parser-output")

# def scrape_r(url):
#     page = requests.get(url)
#     soup = BeautifulSoup(page.text, features="html.parser")

#     title = soup.find("div", class_="page-header__title-wrapper")
#     article = soup.find("div", class_="mw-parser-output")

    
#     article_data = {
#         "title": title.text,
#         "article": article.text
#     }

#     return article_data

# scraped_article = scrape_r(url)

# with open("scraped_article.json", "w") as json_file:
#     json.dump(scraped_article, json_file, indent=4)

with open("scraped_article.json", "r") as file:
    article = json.load(file)

pprint(article)