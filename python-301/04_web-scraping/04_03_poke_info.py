# Use the Pokemon API at https://pokeapi.co/ to assemble a team of your
# six favorite Pokémon.
# Your task is to fetch information about six Pokémon through the
# necessary API calls and include the information in your local script.
# This information should include at least:
# - name
# - number
# - types
#
# You can improve on your project even more by writing the data to a small
# `.html` page which allows you to also display the sprites of each Pokémon.
# Check out the guides they provide: https://pokeapi-how.appspot.com/page5

import requests
from pprint import pprint
from bs4 import BeautifulSoup
import json
import re

url = "https://pokeapi.co/api/v2/pokemon/"

def poke_info(name):
    response = requests.get(url+name)
    data = response.json()

    print("Name:",data["name"])
    print("ID:", data["id"])
    type_data = data["types"]
    type_names = [entry["type"]["name"] for entry in type_data]
    print("Types:", ", ".join(type_names))

poke_info("bulbasaur")
poke_info("charizard")
poke_info("squirtle")