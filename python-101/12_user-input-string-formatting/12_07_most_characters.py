# Write a script that takes three strings from the user
# and prints the longest string together with its length.
#
# Example Input:
#     hello
#     world
#     greetings
#
# Example Output:
#     9, greetings

word_1 = input("Please enter word 1: ")
word_2 = input("PLease enter word 2: ")
word_3 = input("Please enter word 3: ")

if len(word_1) > (len(word_2) or len(word_3)):
    print(len(word_1), word_1)
elif len(word_2) > (len(word_1) or len(word_3)):
    print(len(word_2), word_2)
elif len(word_3) > (len(word_1) or len(word_2)):
    print(len(word_3), word_3)
