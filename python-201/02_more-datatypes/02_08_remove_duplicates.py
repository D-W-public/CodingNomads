# Write code that removes all duplicates from a list.
# Solve this challenge in two ways:
# 1. Convert to a different data type
# 2. Use a loop and a second list to solve it more manually

list_ = [1, 2, 3, 4, 3, 4, 5]



#Loop_solution

list_u=[]

for x in list_:
    if x not in list_u:
        list_u.append(x)
    
print(list_u)

#Data_type solution

s1 = set(list_)

print(s1)