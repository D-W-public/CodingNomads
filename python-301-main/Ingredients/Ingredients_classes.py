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
    