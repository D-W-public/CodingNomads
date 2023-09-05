# All the text in here are Python code comments.
# A Python code comment starts with a hash symbol (#).
# Python will ignore this when running the file.
# You'll see instructions for your labs written in code comments.
# --------------------------------
# Here's your first task:
# Re-create the guess-my-number game from the course.
# Type the whole code out instead of copy-pasting.
# Typing out code, even if you just copy it, trains your coding skills!
# Write your code below:

import random

while True:
    print("Let's play guess the number.")
    user_number = int(input("Please enter an integer between 0-10: "))

    comp_number = random.randint(0, 10)

    try:
        if user_number == comp_number:
            print("Congrats you guessed the number!")
            exit()
        else:
            print("Try again.")

    except TypeError:
        print("Input invalid!")
    
    except ValueError:
        print("Input invalid!")