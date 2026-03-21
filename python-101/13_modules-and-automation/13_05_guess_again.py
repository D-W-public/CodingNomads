# Re-create the guess-my-number game from scratch. Don't peek!
# This time, give your players only a certain amount of tries
# before they lose.

import random

number = random.randint(1, 10)
counter = 5

while counter > 0:
    guess = int(input("Guess a number between 1-10: "))

    if guess == number:
        print("grats you won!")
        break
    else:
        counter -= 1
        print(f"Please try again. You have {counter} trys left.")
