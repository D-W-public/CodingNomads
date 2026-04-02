# Read in all the words from the `words.txt` file.
# Then find and print:

# 1. The shortest word (if there is a tie, print all)
# 2. The longest word (if there is a tie, print all)
# 3. The total number of words in the file.

with open("words.txt") as file_in:
    words = file_in.read().split()

    total_len = len(words)

    min_len = min(len(w) for w in words)
    max_len = max(len(w) for w in words)

    shortest = [w for w in words if len(w) == min_len]
    longest = [w for w in words if len(w) == max_len]

    print(f"{shortest}\n{longest}\n{total_len}")
