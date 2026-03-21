# Extract four words of edible food items from the sentence below.
# Use only string slicing to pick them out!
# Feel free to use pen and paper to number the indices
# and find the locations quicker.
#
# What dish can you make from these ingredients? :)

s = "They grappled with their leggins before going to see the buttercups flourish."

print(f"{s[7:12]}\n{s[26:29]}\n{s[-9:-4]}\n{s[-20:-14]}\n\n{s[7:12]+s[4]+s[8]+s[-4]+s[2]}")
