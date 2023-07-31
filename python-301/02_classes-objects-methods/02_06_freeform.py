# Write a script with three classes that model everyday objects.
# - Each class should have an `__init__()` method that sets at least 3 attributes
# - Include a `__str__()` method in each class that prints out the attributes
#     in a nicely formatted string.
# - Overload the `__add__()` method in one of the classes so that it's possible
#     to add attributes of two instances of that class using the `+` operator.
# - Create at least two instances of each class.
# - Once the objects are created, change some of their attribute values.
#
# Be creative. Have some fun. :)
# Using objects you can model anything you want:
# Animals, paintings, card games, sports teams, trees, people etc...

class Elephant:
    """ Tröööt """
    def __init__(self, name, continet, sex):
        self.name = name
        self.continent = continet
        self.sex = sex

    def __str__(self):
        return f"Name: {self.name} \nOrigin: {self.continent}\nSex: {self.sex}"

class Bike:

    def __init__(self, model, type, color):
        self.model = model
        self.type = type
        self.color = color

    def __str__(self):
        return f"Model: {self.model}\nType:{self.type}\nColor:{self.color}"

class Drink:

    def __init__(self, name, taste, color):
        self.name = name
        self.taste = taste
        self.color = color
    
    def __str__(self):
        return f"{self.name}-Juice has a {self.taste} taste and a {self.color} apperance."

    def __add__(self, other):
        """ Mixes two drinks """
        new_name = self.name + other.name
        new_taste = self.taste + other.taste
        new_color = self.color + other.color
        return Drink(name=new_name,taste=new_taste, color=new_color)

if __name__ == '__main__':

    la = Elephant("Lakshmi", "Asia", "Female")
    ind = Elephant("Indlovu", "Afrika", "Male")

    ra = Bike("Bianchi Oltre", "Roadbike", "black")
    mo = Bike("Cube Aim", "Mountainbike", "white")

    ora = Drink("Orange", "sweet", "orange")
    lem = Drink("Lemon", "sour", "yellow")

    orlem = ora + lem

    print(orlem)