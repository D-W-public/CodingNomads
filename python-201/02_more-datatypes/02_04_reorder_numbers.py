# Read in 10 numbers from the user.
# Place all 10 numbers into an list in the order they were received.
# Print out the second number received, followed by the 4th, 
# then the 6th, then the 8th, then the 10th.
# Then print out the 9th, 7th, 5th, 3rd, and 1st number:
#
# Example input:  1,2,3,4,5,6,7,8,9,10
# Example output: 2,4,6,8,10,9,7,5,3,1

lst1=[]

c = 10

while c > 0:
    user_input = int(input("Please enter int: "))
    lst1.append(user_input)
    c -= 1

print(lst1[1::2]+lst1[-2::-2])


