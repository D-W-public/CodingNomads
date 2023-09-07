# Write a custom exception  that inherits from `Exception()`
# Open and read in the content of the book `.txt` files in the `books/` folder
# like you did in the previous exercise.
# Raise your `PrinceException()` if the first 100 characters of a book
# contain the string "Prince".

class PrinceFound(Exception):
    pass

try:
    with open("python-301/05_exceptions/books/war_and_peace.txt", "r") as file:
        content = file.read(100)
        if "Prince" in content:
            raise PrinceFound("Found him.")

finally:
    file.close()