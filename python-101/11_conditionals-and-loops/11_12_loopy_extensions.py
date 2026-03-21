# Proof that the following file is a .pdf file using a `for` loop.
# - Don't use the string method you've used to solve this before!
# - Don't use the `in` keyword to look for a sub-string!
# - Don't use any string slicing technique either!
#
# You'll see that it'll be tricky to solve this challenge with a loop :)
# Remember to use also other techniques you've learned,
# for example flags and conditional statements.


filename = "operators.pdf"
is_pdf = False

# 1. Reverse the string manually using a loop
reversed_name = ""
for char in filename:
    reversed_name = char + reversed_name

# 2. Check the first 4 characters of the reversed string
# We need to find: 'f', 'd', 'p', '.'
target = "fdp."
match_count = 0

for i in range(4):
    if reversed_name[i] == target[i]:
        match_count += 1

# 3. Use a flag to confirm the proof
if match_count == 4:
    is_pdf = True

print(f"Is the file a PDF? {is_pdf}")
