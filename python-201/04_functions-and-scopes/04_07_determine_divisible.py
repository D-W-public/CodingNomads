# Write a script where you complete the following tasks:
# - define a function that determines whether the number is
#   divisible by 4 OR 7 and returns a boolean
# - define a function that determines whether a number is
#   divisible by both 4 AND 7 and returns a boolean
# - take in a number from the user between 1 and 1,000,000,000
# - call your functions, passing in the user input as the arguments,
#   and set their output equal to new variables 
# - print your the result variables with descriptive messages


number = int(input("Pleas enter a number: "))

def or_funct(number):
    or_ = False
    if number % 4 == 0 or number % 7 == 0:
        or_ = True
    return or_

def and_funct(number):
    and_ = False
    if number % 4 == 0 and number % 7 == 0 :
        and_ = True
    return and_


or_1 = or_funct(number)

and_1 = and_funct(number)

print(f"""
The number {number}
is divisible by 4 or 7 : {or_1}
is divisible by 4 and 7: {and_1}""")