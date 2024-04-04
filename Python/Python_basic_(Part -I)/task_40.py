"""
40. Write a Python program to calculate the distance between the points (x1, y1) and (x2, y2). 

Link: https://www.w3resource.com/python-exercises/python-basic-exercise-40.php
"""

# Solution
import math

x1 = float(input("x1 = "))
y1 = float(input("y1 = "))
x2 = float(input("x2 = "))
y2 = float(input("y2 = "))

print(f"Points A({x1},{y1}), B({x2},{y2})")

distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

print(f"Distance between Points A and B = {distance} Units")
