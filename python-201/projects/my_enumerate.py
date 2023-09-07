# Reproduce the functionality of Python's built-in `enumerate()` function.
# Define a function called `my_enumerate()` that takes an iterable as input
# and gives back both the element as well as its index position as an integer.

def my_enumerate(iterable, start=0): 
      index = start
      for item in iterable:
            yield index, item
            index +=1


fruits = ["banana", "pear", "grape","apple"]

for index, fruit in my_enumerate(fruits, start=0):
      print(f"Index: {index}:  {fruit}")
