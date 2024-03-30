"""
Write a Python program that returns true if the two given integer values are 
equal or their sum or difference is 5.
"""

# Solution

def function(a, b):
    value = True
    if a != b and a + b != 5 and abs(a - b) != 5:
        value = False
    return value

a = int(input("Enter a: "))
b = int(input("Enter b: "))

print(function(a, b))
