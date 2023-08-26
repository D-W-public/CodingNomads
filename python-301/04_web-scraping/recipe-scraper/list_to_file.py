import requests
from bs4 import BeautifulSoup
import json

def scrape_r(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, features="html.parser")

    title = soup.find("h1", class_="title")
    author = soup.find("p", class_="author")
    recipe = soup.find("div", class_="md")

    recipe_data = {
        "title": title.text,
        "author": author.text.strip("by "),
        "recipe": recipe.text
    }

    return recipe_data

def read_url_list(filename):
    with open(filename, "r") as f:
        urls = [line.strip() for line in f]
        return urls

urls = read_url_list("list_of_links.txt")

scraped_data = []

for url in urls:
    print("Scraping: ", url)
    recipe_data = scrape_r(url)

    if recipe_data:
        scraped_data.append(recipe_data)

with open("scraped_recipes.json", "w") as json_file:
    json.dump(scraped_data, json_file, indent=4)