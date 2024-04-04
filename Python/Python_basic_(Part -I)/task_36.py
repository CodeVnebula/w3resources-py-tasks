"""
Write a Python program to add two objects if both objects are integers.
"""

# Solution

def add_numbers(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
        return "Inputs must be integers!"
    return a + b

print(add_numbers(4, 2))    
print(add_numbers(23, 2.54)) 
print(add_numbers('6', 8))     
print(add_numbers('12', '2')) 
