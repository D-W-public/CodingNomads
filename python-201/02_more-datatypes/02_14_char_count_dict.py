# Write a script that takes a text input from the user
# and creates a dictionary that maps the letters in the string
# to the number of times they occur. For example:
#
# user_input = "hello"
# result = {"h": 1, "e": 1, "l": 2, "o": 1}


keys = []

values = []

tup  = tuple(input("Please enter a sting: "))

for i in tup:
    keys.append(i)

for c in tup:
    values.append(tup.count(c))


dict_1 = dict(zip(keys, values))

print(dict_1)