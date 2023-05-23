# Write a script that takes a string of words and a symbol from the user.
# Replace all occurrences of the first letter with the symbol. For example:
#
# String input: more python programming please
# Symbol input: §
# Result: §ore python progra§§ing please

old_str = input("Please enter string: ")
new_str = old_str.replace("a", "@")
print(new_str)