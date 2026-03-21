# Create a sarcastic program that asks a user for their honest opinion,
# then prints the same sentence back to them in aLtErNaTiNg CaPs.

text = str(input("Please enter a text: "))

result = ""

for i, c in enumerate(text):
    if i % 2 == 0:
        result += c.lower()
    elif i % 2 != 0:
        result += c.capitalize()

print(result)

