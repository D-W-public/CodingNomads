# Create two classes that model a rectangle and a circle.
# The rectangle class should be constructed by length and width
# while the circle class should be constructed by radius.
#
# Write methods in the appropriate class so that you can calculate
# the area of both the rectangle and the circle, the perimeter
# of the rectangle, and the circumference of the circle.

import math

class Rectangle:

    def __init__ (self, length, width):
        self.length = length
        self.width = width

    def __str__(self):
        return f"\n Length : {self.length} \n Width : {self.width} \n"
    
    def perimeter(self):
        perimeter = 2 * (self.length + self.width)
        return f"The perimeter of the rectangle is: {perimeter}"


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def circumference(self):
        circumference = 2 * math.pi * self.radius
        return f"The circumfence of the circle is: {circumference}"

c = Circle(5)

r = Rectangle(3, 5)

print(r.perimeter())

print(c.circumference())