# Ask your user for a number between 0 and 1,000,000,000.
# Use a `while` loop to find the number. When the number is found,
# exit the loop and print the number to the console.

user_number = int(input("Please enter a number(int): "))

count = 0

while user_number < 1000000000:
    while count < user_number:
     count += 1
    if count == user_number:
         print(count)
         break