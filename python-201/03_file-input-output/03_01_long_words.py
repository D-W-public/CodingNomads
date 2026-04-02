# Write a program that reads in `words.txt` and prints only the words
# that have more than 20 characters (not counting whitespace).


with open("words.txt") as file_in:
    content = file_in.read()
    words = content.split()
    for word in words:
        if len(word) > 20:
            print(word)
