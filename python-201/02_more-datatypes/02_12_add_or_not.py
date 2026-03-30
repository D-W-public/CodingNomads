# MEMORY GAME WITH SETS
# Continuously collect number input from a user with a `while` loop.
# Confirm that the input can be converted to an integer,
# then add it to a Python `set()`.
# If the element was already in the set, notify the user that their
# their input is a duplicate and deduct a point.
# If the user loses 5 points, quit the program.
# They win if they manage to create a set that has more than 10 items.

import sys

counter = 5

uniques = set()

while counter > 0:
    x = int(input("Please enter 10 unique ints to win the game: "))
    if len(uniques) < 10:
        if x not in uniques:
            uniques.add(x)
        else:
            counter -= 1
            print(f"You tried this one already.\nYou have {counter} tries remaining.")
    else:
        print("Congrats you won the game...")
        sys.exit()
