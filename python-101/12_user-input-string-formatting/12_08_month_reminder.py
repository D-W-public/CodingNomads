# Take in a number between 1 and 12 from the user
# and print the name of the associated month:
# "January", "February", ... "December"
# Print "Error" if the number from the user is not between 1 and 12.
# Use a nested `if` statement.

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

i = int(input("Pleease input a number: "))

if i in range(1,13):
    print(months[i])
else:
    print("invalid input")
