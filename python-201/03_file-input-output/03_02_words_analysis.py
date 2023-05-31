# Read in all the words from the `words.txt` file.
# Then find and print:

# 1. The shortest word (if there is a tie, print all)
# 2. The longest word (if there is a tie, print all)
# 3. The total number of words in the file.


with open("words.txt", "r") as file:
    words = file.read().split()

shortest_length = len(min(words, key=len))
shortes_words = [word for word in words if len(word) == shortest_length]

longest_length = len(max(words, key=len))
longest_word = [word for word in words if len(word) == longest_length]

w_count = len(words)

print("The shortest word(s) is/ are:", *shortes_words, sep="\n")
print("The longest word(s) is/are: ", *longest_word, sep="\n" )
print("The total word count is: ", w_count)