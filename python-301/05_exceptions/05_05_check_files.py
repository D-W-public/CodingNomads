# Read in the first number from `integers.txt`
# and perform a calculation with it.
# Make sure to catch at least two possible Exceptions (`IOError` and `ValueError`)
# with specific `except` statements, and continue to do the calculation
# only if neither of them applies.

file_name = 'integers.txt'
integers = []

try:
    with open(file_name, "r") as f:
        for item in f:
            integers.append(int(item))
        try:
            a = integers[0]
            print(a*2)
        except ValueError:
            print("Invalid input")
        
except IOError:
    print("Something worng with the file.")

finally:
    f.close()