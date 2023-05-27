# Convert some sequences you got to know into other sequences:
# - Convert the string shown below into a tuple.
# - Convert the tuple into a list.
# - Change the `c` character in your list into a `k`
# - Convert the list back into a tuple.

string = "codingnomads"

a = tuple(string)

lst1 = []

for x in a:
    lst1.append(x)


lst1[0] = "k"

lst1 = tuple(lst1)

print(lst1)
print(type(lst1))



