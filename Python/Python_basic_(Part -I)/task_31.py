"""
Write a Python program that computes the greatest common divisor (GCD) of two positive integers.
"""

# Solution

a = int(input("Enter num a: "))
b = int(input("Enter num b: "))
org_a = a
org_b = b
while a != b:
    if a > b:
        a -= b
    elif b > a:
        b -= a

print(f'(GCD) of {org_a} and {org_b} is {a}')
