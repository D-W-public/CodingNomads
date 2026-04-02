# Write a script that reads in the contents of `words.txt`
# and writes the contents in reverse to a new file `words_reverse.txt`.

with open("words.txt") as file_in:
    lines = file_in.readlines()

    with open("r_words.txt", "w") as file_out:
        file_out.writelines(reversed(lines))
