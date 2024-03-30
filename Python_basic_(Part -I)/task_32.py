"""
Write a Python program to find the least common multiple (LCM) of two positive integers.
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

gcd = a
lcm = abs(org_a * org_b)//gcd

print(f'(LCM) of {org_a} and {org_b} is {lcm}')
