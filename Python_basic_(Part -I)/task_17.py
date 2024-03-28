"""
Write a Python program to test whether a number is within 100 of 1000 or 2000.
"""

# Solution

def is_near(n):
    return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))

print(is_near(1050))    # True
print(is_near(2150))    # False
print(is_near(899))     # False
