# Write a script that takes in a string from the user.
# Using the `split()` method, create a list of all the words in the string
# and print back the most common word in the text.
from collections import Counter

text = str(input("Please enter text: "))
words = text.split()
most_common_word = Counter(words).most_common(1)[0][0]

print(most_common_word)

