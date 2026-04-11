# Combine the `greet()` function that you developed in the course materials
# with the `write_letter()` function from the previous exercise.
# Write both functions in this script and call `greet()` within `write_letter()`
# to let `greet()` take care of creating the greeting string.

name = "Ralf"
text = "blubls"
greeting = "Hi"


def write_letter(name, text):

    def greet(greeting: str, name: str) -> str:
        sentence = f"{greeting}, {name}! How are you?"
        return sentence

    print(greet(greeting, name))
    print(text)
    print(f"Goodbey {name}.")


write_letter(name, text)
