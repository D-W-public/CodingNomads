# In this exercise, you will practice both File I/O as well as using Exceptions
# in a real-world scenario.
#
# This folder contains another folder called `books/` that contains three text files
# of books from Project Gutenberg:
# 1. war_and_peace.txt
# 2. pride_and_prejudice.txt
# 3. crime_and_punishment.txt
#
# 1) Open `war_and_peace.txt`, read the whole file content and store it in a variable
# 2) Open `crime_and_punishment.txt` and overwrite the whole content with an empty string
# 3) Loop over all three files and print out only the first character each. Your program
#    should NEVER terminate with a Traceback.
#     a) Which exception can you expect to encounter? Why?

""" An error like IndexError, because one of the txt files has been emptied."""

#     b) How do you catch it to avoid the program from terminating with a traceback?


war = "python-301/05_exceptions/books/war_and_peace.txt"
crime = "python-301/05_exceptions/books/crime_and_punishment.txt"
pride = "python-301/05_exceptions/books/pride_and_prejudice.txt"
file_names = [war, crime, pride]

# try:

#     with open(war, "r") as file:
#         war = file.read()

# except IOError:
#     print("Something is wrong with this file.")


# finally:
#     file.close()
# try:

#     with open(crime, "w") as file:
#         file.write("")
# except IOError:
#     print("Something is wring with that file")
# finally:
#     file.close()

try:
    for file_name in file_names:
        try:
            with open(file_name, "r") as file:
                content = file.read()
                first_character = content[0]
                print(f"First Character of {file_name}: {first_character}")
            
        except (IOError, IndexError) as e:
            if isinstance(e, IOError):
                print(f"Error opening {file_name}.")
            elif isinstance(e, IndexError):
                print(f"{file_name} Index not found or file empty.\n")
           
finally:
    for file_name in file_names:
        file.close()
