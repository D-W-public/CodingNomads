# Write a script that takes a string input from a user
# and prints a total count of how often each individual vowel appeared.

text = str(input("Please enter a text: "))

text = text.lower()

a = 0
e = 0
i = 0
o = 0
u = 0

for c in text:
    if c == "a":
        a += 1
    elif c == "e":
        e += 1
    elif c == "i":
        i += 1
    elif c == "o":
        o += 1
    elif c == "u":
        u += 1

print(f"A:{a} E:{e} I:{i} O:{o} U:{u}")
