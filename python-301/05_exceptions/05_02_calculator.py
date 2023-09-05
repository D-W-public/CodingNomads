# Write a script that takes in two numbers from the user and calculates the quotient.
# Use a try/except statement so that your script can handle:
#
# - if the user enters a string instead of a number
# - if the user enters a zero as the divisor
#
# Test it and make sure it does not crash when you enter incorrect values.
while True:
    try:
        print("Let's divide some numbers.")
        a = int(input("Enter first numeber: "))
        b = int(input("Enter second number: "))
        print(a/b)

    except TypeError:
        print("Please eneter a number")

    except ZeroDivisionError:
        print("This is against the law!")
