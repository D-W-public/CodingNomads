# Write a script that takes a string of words and a symbol from the user.
# Replace all occurrences of the first letter with the symbol. For example:
#
# String input: more python programming please
# Symbol input: §
# Result: §ore python progra§§ing please

text = input("Please enter a string: ")

symbol = str(input("Please enter a symbol: "))


words = text.split()

new_list = [symbol + w[1:] for w in words if len(w) > 0]

result = " ".join(new_list)

print(result)
