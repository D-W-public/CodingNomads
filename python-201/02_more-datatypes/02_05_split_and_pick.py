# Write a script that takes in a string from the user.
# Using the `split()` method, create a list of all the words in the string
# and print back the most common word in the text.

from collections import defaultdict

lst1 = []
count = defaultdict(int)
inp = input("Pleae enter a sentence: ")
lst1.append(inp)

for sub in lst1:
    for word in inp.split(" "):
        count[word] += 1

result = max(count, key=count.get)

print(f"{result} is the most used word in given string.")