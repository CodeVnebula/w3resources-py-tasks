"""
Write a Python program to get the volume of a sphere with radius six.
"""

# Solution

import math

radius = int(input("Enter radius: "))
pi = math.pi
volume = '%.3f'%(4/3 * pi * pow(radius, 3))
print(f"Volume of the circle with radius {radius} = {volume}")
