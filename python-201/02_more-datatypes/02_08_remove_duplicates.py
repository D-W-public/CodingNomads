# Write code that removes all duplicates from a list.
# Solve this challenge in two ways:
# 1. Convert to a different data type
# 2. Use a loop and a second list to solve it more manually

list_ = [1, 2, 3, 4, 3, 4, 5]

set_1 = set(list_)
print(set_1)

list_no_dup = []

for x in list_:
    if x not in list_no_dup:
        list_no_dup.append(x)

print(list_no_dup)
