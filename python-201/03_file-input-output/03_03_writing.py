# Write a script that reads in the contents of `words.txt`
# and writes the contents in reverse to a new file `words_reverse.txt`.
from pathlib import Path

words = Path("/home/jayram/Documents/CodingNomads/python-201/03_file-input-output/words.txt")

with open(words, "r") as file:
    words = file.read().split()

rev_w = reversed(words)

with open("reversed.txt", "w") as file:
    for word in rev_w:
        file.write(word + "\n")