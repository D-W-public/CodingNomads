# Create a `Planet()` class that models attributes and methods of
# a planet object.
# Use the appropriate dunder method to get informative output with `print()`

class Planet():
    
    def __init__(self,name, position, mass, cla):
        self.name = name
        self.position = position
        self.mass = mass
        self.cla = cla

    def __str__(self):
        return f"""
        Name:                    {self.name}
        Position in Solarsytem:  {self.position}
        Mass:                    {self.mass} Earth masses (M⊕)
        Class:                   {self.cla}
        """

Jup = Planet("Jupiter", 5, 317.8, "J (gas giant)")

print(Jup)