"""
Write a Python program that will accept the base and height of a triangle and compute its area.
"""

# Solution

def calculate_area(base, height):
    area = (base * height) / 2
    return area

base = float(input("Enter base of triangle: "))
height = float(input("Enter height of triangle: "))

area = calculate_area(base, height)

print(f'Area = {area}')
