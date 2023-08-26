# For this project, your task is to create a CLI that takes as an input
# the names of ingredients from a user. Then, your code will fetch
# the recipe information from the CodingNomads recipe collection,
# and search through the text of the recipes to find ones that include
# the provided ingredients.
#
# Note: Feel free to integrate your custom Ingredient() and Soup() classes
# into the code base, to get some additional practice in working with your
# custom Python classes.

URL = "https://codingnomads.github.io/recipes"

import re
import json

def ingredient_look_up(recipes, Ingredient):
    matches = []

    for recipe in recipes:
        if "recipe" in recipe:
            recipe_text = recipe["recipe"]
            ingredient_lines = re.findall(r'INGREDIENTS:(.*?)\n\n', recipe_text, re-DOTALL | re.IGNORECASE)
