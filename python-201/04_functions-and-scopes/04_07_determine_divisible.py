# Write a script where you complete the following tasks:
# - define a function that determines whether the number is
#   divisible by 4 OR 7 and returns a boolean
# - define a function that determines whether a number is
#   divisible by both 4 AND 7 and returns a boolean
# - take in a number from the user between 1 and 1,000,000,000
# - call your functions, passing in the user input as the arguments,
#   and set their output equal to new variables
# - print your the result variables with descriptive messages

x = float(input("Please enter a number to check divisability: "))


def or_func(x):
    if x % 4 == 0 or x % 7 == 0:
        or_x = True

    else:
        or_x = False
    return or_x


def and_func(x):
    if x % 4 == 0 and x % 7 == 0:
        and_x = True
    else:
        and_x = False
    return and_x


result_or = or_func(x)
result_and = and_func(x)

print("The number you entered is divisible by:")
print(f"4 or  7 : {result_or}")
print(f"4 and 7 : {result_and}")
