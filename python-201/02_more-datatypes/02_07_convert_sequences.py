# Convert some sequences you got to know into other sequences:
# - Convert the string shown below into a tuple.
# - Convert the tuple into a list.
# - Change the `c` character in your list into a `k`
# - Convert the list back into a tuple.

string = "codingnomads"

tup_conversion = tuple(string)
ls_conversion = list(tup_conversion)
# chaneging the character
ls_conversion[0] = "k"
final_con = tuple(ls_conversion)
print(final_con)
