# Write a script that takes a string input from a user
# and prints a total count of how often each individual vowel appeared.


text = input("Please enter text, to count vowels: ")

count = 0
vowels = ("a","A","e","E","i","I","o","O","u","U")

for char in text:
    if char in vowels:
        count += 1

print("Vowels in text: ", count)