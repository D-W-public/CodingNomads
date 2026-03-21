# Write a script that takes a string of words and a letter from the user.
# Find the index of first occurrence of the letter in the string. For example:
#
# String input: hello world
# Letter input: o
# Result: 4

text = input("Please enter a word: ")

letter = input("Please enter a letter: ")

for c in text:
    if c == letter:
        print(text.index(c))
