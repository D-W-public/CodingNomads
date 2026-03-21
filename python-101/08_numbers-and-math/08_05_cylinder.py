# Write the necessary code calculate the volume and surface area
# of a cylinder with a radius of 3.14 and a height of 5.
# Print out the result.

from math import pi

r = 3.14
h = 5

V = pi*r**2*h
A = 2*pi*(h+r)

print(V,A)

