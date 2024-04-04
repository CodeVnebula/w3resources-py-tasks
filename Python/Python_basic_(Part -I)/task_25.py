"""
   Write a Python program that checks whether a specified value is contained within a group of values.
Test Data :
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False
"""

# Solution

import random

random_list = [random.randint(-10, 10) for _ in range(10)]

def check_value(random_list, n):
    result = False
    for i in range(len(random_list)):
        if n == random_list[i]:
            result = True
            break
    return result

n = int(input("Enter n: "))

result = check_value(random_list, n)
print(f'{n} -> {random_list} : {result}')
