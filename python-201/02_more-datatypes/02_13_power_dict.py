# Write a script that creates a dictionary of keys, `n`
# and values `n * n` for numbers 1 to 10. For example:
# result = {1: 1, 2: 4, 3: 9, ... and so on}

dict_1 = {}

keys = range(11)

values = []

a = None

for i in keys:
    a = i*i
    values.append(a)


for k in keys:
    dict_1[k] = values[k]


print(dict_1)