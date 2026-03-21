# Write a Hangman game in Python.
# Users should have a limited amount of attempts to guess a pre-defined word.
# Print feedback to the user when they made a guess,
# and keep track of and communicate their remaining attempts.
# Hard-code a word that needs to be guessed in the script
# Print an explanation to the user
# Display the word as a sequence of blanks, e.g. "_ _ _ _ _" for "hello"
# Ask for user input
# Allow only single-character alphabetic input
# Create a counter for how many tries a user has
# Keep asking them for their guess until they won or lost
# When they find a correct character, display the blank with the word
#   filled in, e.g.: "_ e _ _ _" if they guessed "e" from "hello"
# Display a winning message and the full word if they win
# Display a losing message and quit the game if they don't make it

import sys

word = "slipknot"
guessed_word = ["_"] * len(word)
trys = 10
guessed_letters = []

print("""
Hello player!
Welcome to hangman.
Let's see if you can save this poor soul...""")

print(" ".join(guessed_word))

while trys > 0 and "_" in guessed_word:
    print(f"\nTrys = {trys}")

    guess = input("\nPlease enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Only one letter(!) at a time please!")
        continue

    if guess in guessed_letters:
        trys -= 1
        print(
            f"You already tried this one.\nDont waste you attemps like this\n{trys}\n"
        )
        continue

    guessed_letters.append(guess)

    if guess in word:
        print(f"Sweet! {guess} is in there.")

        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess

    else:
        trys -= 1
        print("Nope try again!")

    print(" ".join(guessed_word))

# Adding shutdown sequence

if "_" not in guessed_word:
    print("\nWhoop whoop he lives a nother day!")
    sys.exit()

else:
    print("\nPress F to pay respect")
    sys.exit()
