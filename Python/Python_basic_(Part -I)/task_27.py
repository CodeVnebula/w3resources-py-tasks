"""
Write a Python program that concatenates all elements in a list into a string and returns it.
"""

# Solution

import random

random_list = [random.randint(0, 50) for _ in range(10)]

def concatenate_elements(random_list):
    concatenated = ''
    for i in range(len(random_list)):
        concatenated += str(random_list[i])
    return concatenated

result = concatenate_elements(random_list)
print(result)
