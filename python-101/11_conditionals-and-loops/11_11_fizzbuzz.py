# You start this journey with a number `n`.
# You have to display a string representation of all numbers from 1 to n,
# but there are some constraints:
# - If the number is divisible by 3, write `Fizz` instead of the number
# - If the number is divisible by 5, write `Buzz` instead of the number
# - If the number is divisible by both 3 and 5, write `FizzBuzz` instead of the number
import math

n = range(1,16)
a = "Fizz"
b = "Buzz"
for i in n:
#    if i % 3 == 0:
#        print(a)
#        if i % 5 == 0:
#            print(a+b)
#    elif i % 5 == 0:
#        print(b)
#    else:
#           print(i)
    
    if i % 3 == 0 and i % 5 == 0:
        print(a,b)
    elif i % 3 == 0:
        print(a)
    elif i % 5 == 0:
        print(b)
    #if i % 3 == 0 and i % 5 == 0:
    #    print(a,b)
    else:
           print(i)
