class Ingredient:

    """Models a food item used as ingredient"""

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def expire(self):
        """Exipers the ingredient"""
        print(f"{self.name} has expired.")
        self.nname = "expired " + self.name

    def __str__(self):
        return f"{self.name} ({self.amount})"
    
    def __repr__(self):
        return f"Ingredient(name={self.name}, amount={self.amount})"

class Spice(Ingredient):
    """Models a spice to flavor your food."""

    def grind(self):
        print(f"You have now {self.amount} of ground {self.name}.")



class Vegeteable(Ingredient):
    """ Veggie class """
    def cut(self):
        """ Cuts the Veggie """
        print(f"{self.name} is cut.")