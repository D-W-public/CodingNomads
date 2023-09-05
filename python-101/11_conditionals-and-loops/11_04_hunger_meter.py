# Your hunger-meter currently only handles string input accurately.
# Replace your first `if` statement with a type check.
# If the value of `hunger` is not of the type `str`,
# print a message that reminds you to
# declare your hunger levels with a string.

while True:
    hunger = input("Please enter your hunger level: ")

    try:
        hunger_as_int = int(hunger)
        print("Invalid input, please enter a string.")
    except ValueError:
        if hunger.lower() == "big":
            print("Eat the pizza")
            exit()
        elif hunger.lower() == "small":
            print("Eat the apple.")
            exit()
        else:
            print("Invalid input. Please choose between big/small")
