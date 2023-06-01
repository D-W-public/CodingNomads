import string

#creating a funct to count
#setting up the "empty" dict to feed the count in 
def counter(text):
    counts = {
        "Lower case": 0,
        "Upper case" : 0,
        "Punctuation": 0,
        "Total":0
    }

    for char in text:
        if char.islower():
            counts["Lower case"] +=1
        elif char.isupper():
            counts["Upper case"] +=1
        elif char in string.punctuation:
            counts["Punctuation"] +=1

        if char != " ":
            counts["Total"] += 1
    
    return counts

user_input = input("Please enter text: ")

result = counter(user_input)

print(f"""
Upper case letters: {result["Upper case"]}
Lower case letters: {result["Lower case"]}
Punctuation:        {result["Punctuation"]}

Total letters:      {result["Total"]}""")