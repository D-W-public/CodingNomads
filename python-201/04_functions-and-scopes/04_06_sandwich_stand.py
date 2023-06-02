# Write a function called `make_sandwich()` that sticks to the following:
# - takes a type of bread as its first, required argument
# - takes an arbitrary amount of toppings
# - returns a string representing a sandwich with the bread on top
#   and bottom, and the toppings in between.




def make_sandwich(bread,*fillings):

    sandwich = []
    sandwich.append(bread)
    for item in fillings:
        sandwich.append(item) 
    sandwich.append(bread)
    for item in sandwich:    
        print(f"{item}")

make_sandwich("Whole wheat bread", "tomat","cheese","bacon")