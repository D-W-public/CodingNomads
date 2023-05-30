# MEMORY GAME WITH SETS
# Continuously collect number input from a user with a `while` loop.
# Confirm that the input can be converted to an integer,
# then add it to a Python `set()`.
# If the element was already in the set, notify the user that their
# their input is a duplicate and deduct a point.
# If the user loses 5 points, quit the program.
# They win if they manage to create a set that has more than 10 items.
points = 0
numbers = set()

while points > -5 and len(numbers) <= 10:
    user_input = input("Enter a number: ")
    
    try:
        number = int(user_input)
        if number in numbers:
            print("Duplicate number! -1 point")
            points -= 1
        else:
            numbers.add(number)
            points += 1
    except ValueError:
        print("Invalid input! Please enter a number.")

if points <= -5:
    print("You lost! Better luck next time.")
else:
    print("Congratulations! You won!")