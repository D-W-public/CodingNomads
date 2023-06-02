# Combine the `greet()` function that you developed in the course materials
# with the `write_letter()` function from the previous exercise.
# Write both functions in this script and call `greet()` within `write_letter()`
# to let `greet()` take care of creating the greeting string.

name = input("Please enter your name: ")

text = f"""
I hope this letter finds you well. I will not make it to this years conference, 
due to the rising cost of litteraly everything.
Take care {name}"""


def hello(greeting, name):
        sentence = f"{greeting}, {name}. Nice to see you here."
        return sentence


def write_letter(name,text):
    letter = hello("Hi", name) + text
    return letter

print(write_letter(name, text))
    