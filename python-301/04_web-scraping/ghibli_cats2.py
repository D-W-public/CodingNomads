import requests
from pprint import pprint
import re
import json

#getting the sub-links from the ghibli API for all cat characters and the films they apear in
"""
url = "https://ghibliapi-iansedano.vercel.app/api/species/"

response = requests.get(url)

data = response.json()

cat_list = []
film_list = []
#pprint(data["data"]["species"][4]["people"])

for person in data["data"]["species"][4]["people"]:
    links = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', person)
    cat_list.extend(links)


for film in data["data"]["species"][4]["films"]:
    links = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', film)
    film_list.extend(links)

with open("cat_list.txt", "w") as f:
    for item in cat_list:
        f.write(str(item) +"\n")

with open("film_list.txt", "w") as f:
    for item in film_list:
        f.write(str(item) + "\n")
"""


#Accesing the stored links to further extract data (CATS)

"""
cats_dict = {}

def link_reader(filename):
    with open(filename, "r") as f:
        urls = [line.strip() for line in f]
        return urls

def cat_extractor(url):
    response = requests.get(url)
    data = response.json()

    cat_data = {
        "name": data["data"][0]["name"],
        "age": data["data"][0]["age"],
        "eye_color": data["data"][0]["eye_color"],
        "hair_color": data["data"][0]["hair_color"],
    }

    return cat_data

urls = link_reader("cat_list.txt")

scraped_cats = []

for url in urls:
    cat_data = cat_extractor(url)

    if cat_data:
        scraped_cats.append(cat_data)


with open("cat_data.json", "w") as json_file:
    json.dump(scraped_cats, json_file, indent=4)

"""

#getting all the film names with cats in them
"""
def link_reader(filename):
    with open(filename, "r") as f:
        urls = [line.strip() for line in f]
        return urls

def film_extractror(url):
    response = requests.get(url)
    data = response.json()

    films_cat_data = {
        "title": data["data"][0]["title"],
        "og_title": data["data"][0]["original_title"],
        "plot": data["data"][0]["description"],
        "director": data["data"][0]["director"],
        "release": data["data"][0]["release_date"]
    }

    return films_cat_data

urls = link_reader("film_list.txt")

scraped_films = []

for url in urls:
    film_cat_data = film_extractror(url)

    if film_cat_data:
        scraped_films.append(film_cat_data)

with open("film_cat_data.json", "w") as json_file:
    json.dump(scraped_films, json_file, indent=4)

"""

