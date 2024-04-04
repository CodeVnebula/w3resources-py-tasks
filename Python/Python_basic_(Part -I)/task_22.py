"""
Write a Python program to count the number 4 in a given list.
"""

# Solution

import random

random_list = [random.randint(0, 10) for _ in range(10)]

def count_element(random_list):
    count = 0
    for i in random_list:
        if i == 4:
            count += 1
    return count

count = count_element(random_list)

print(f'There are {count} "{4}" in the list')
