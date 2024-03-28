"""
Write a Python program to calculate the difference between a given number and 17. 
If the number is greater than 17, return twice the absolute difference.
"""

# Solution

NUM = 17
num = int(input('Enter a number: '))

if num > NUM:
    difference = 2 * abs(num - NUM)
    print(f'2x Difference: {difference}')
else:
    difference = abs(num - NUM)
    print(f'Difference {difference}')
