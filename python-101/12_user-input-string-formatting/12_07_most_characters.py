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

# create  list

lst = []

#ask question 3 times

for i in range(3):
    lst.append(input("Please enter a string: "))
    
#process list items find the longest string

res = max(lst, key=len)
#print longest string plus string length

print("The longest string was: ", res,"with a length of", len(res))