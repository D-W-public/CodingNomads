# Research for interesting APIs online and pick two. You can also use APIs that
# you've already worked with in the course if you prefer.
# Write a program that makes calls to both APIs and find a way to combine the
# data that you receive from both of them.
# E.g.: You could use the Ghibli API to find all ghosts from their films, and
#       create an opposing team of Ghost Pokémon from the Poke API.

import requests
from pprint import pprint

url_1 = "http://numbersapi.com/"
url_2 = "https://api.isevenapi.xyz/api/iseven/"

chosen_one = input("Pleaser enter a number: ")

def numberino(chosen_one):
    response = requests.get(url_1+chosen_one)
    response_2 = requests.get(url_2+chosen_one)
    data = response_2.json()
    print(response.text)
    print(f"Is even: ",data["iseven"])

numberino(chosen_one)