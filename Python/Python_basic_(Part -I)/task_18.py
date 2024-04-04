"""
Write a Python program to calculate the sum of three given numbers. 
If the values are equal, return three times their sum.
"""

# Solution

def _sum(a, b, c):
    if a == b == c:
        return a * 3
    else:
        return a + b + c

a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

print(f'Sum = {_sum(a, b, c)}')
