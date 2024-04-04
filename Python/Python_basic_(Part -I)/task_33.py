"""
Write a Python program to sum three given integers. However, if two values are equal, the sum will be zero.
"""

# Solution

def sum_numbers(a, b, c):
    if a == b or a == c or b == c:
        return 0
    else:
        return a + b + c

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

_sum = sum_numbers(a, b, c)
print("Sum = ", _sum)
