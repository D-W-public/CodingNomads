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

def ingredient_look_up(recipes, ingredient):
    matches = []

    for recipe in recipes:
        if "recipe" in recipe:
            recipe_text = recipe["recipe"]
            ingredient_lines = re.findall(r'INGREDIENTS(.*?)\n\n', recipe_text, re.DOTALL | re.IGNORECASE)

        for ingredient_line in ingredient_lines:
            if re.search(r'\b' + re.escape(ingredient) + r'\b', ingredient_line, re.I):
                matches.append((recipe["title"], recipe["recipe"]))
    return matches

def main():

    with open("/home/jay_ram/Documents/CodingNomads/scraped_recipes.json", "r") as file:
        recipes = json.load(file)

    target_ingredient = input(f"Welcome to the recipe-libary\nPlease enter ingredient: ")

    matching_recipes = ingredient_look_up(recipes, target_ingredient)

    if matching_recipes:
        print(f"\nFound {len(matching_recipes)} recipes using {target_ingredient}\n")
        for recipe_title, recipe_recipe in matching_recipes:
            print(f"\nName: {recipe_title}\n\n{recipe_recipe}\n"+("-"*66))

if __name__ == "__main__":
    main()