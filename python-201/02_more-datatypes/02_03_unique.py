# Write code that creates a list of all unique values in a list.
# For example:
#
from collections import Counter

list_ = [1, 2, 6, 55, 2, "hi", 4, 6, 1, 13]
counts = Counter(list_)
# unique_list = [55, 'hi', 4, 13]

unique_list = [item for item, count in counts.items() if count == 1]

print(unique_list)
