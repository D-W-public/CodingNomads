# Write code that creates a list of all unique values in a list.
# For example:
#
# list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
# unique_list = [55, 'hi', 4, 13]

list1 = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]

unique_list = []

for x in list1:
    if x not in unique_list:
        unique_list.append(x)
    elif x in unique_list:
        unique_list.remove(x)

print(unique_list)