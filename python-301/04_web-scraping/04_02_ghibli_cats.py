# Read through the documentation of the Ghibli API and reproduce the example
# listed at https://ghibliapi.herokuapp.com/#section/Use-Case in Python.
# Try skim the Haskell code example and see if you can understand anything.
# Don't worry if you don't, it's a completely different language :)
#
# Your task is to use the API to find information about all the cats that
# appear in Studio Ghibli films.

BASE_URL = "https://ghibliapi.herokuapp.com/"


import requests
from pprint import pprint
from bs4 import BeautifulSoup
import re
import json


# response = requests.get("https://ghibliapi-iansedano.vercel.app/api/films")
# data = response.json()

# with open("ghibli_films.json", "w") as json_file:
#     json.dump(data, json_file, indent=4)


# with open("ghibli_films.json", "r") as file:
#     ghibli_films = json.load(file)

# #pprint(ghibli_films["data"]["films"][0]["title"])

# def character_find(character):
#     with open("ghibli_films.json", "r") as file:
#         ghibli_films = json.load(file)
    
#     matches = []

#     target = input(f"Welcome to the Ghibli-db.\nWho are you looking for?: ")

#     for character in films:
#         if character.match(ghibli_films["data"]["films"][:][""])

response = requests.get("https://ghibliapi-iansedano.vercel.app/api/people/6b3facea-ea33-47b1-96ce-3fc737b119b8")

data = response.json()

pprint(data)