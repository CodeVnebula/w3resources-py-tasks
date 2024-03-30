"""
Write a Python program to sum two given integers. However, if the sum is between 15 and 20 it will return 20.
"""

# Solution

def sum_numbers(a, b):
    if 15 <= a + b <= 20:
        return 20
    else:
        return a + b

a = int(input("Enter a: "))
b = int(input("Enter b: "))

_sum = sum_numbers(a, b)
print("Sum = ", _sum)
