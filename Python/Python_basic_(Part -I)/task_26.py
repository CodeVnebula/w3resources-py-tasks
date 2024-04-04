"""
 Write a Python program to create a histogram from a given list of integers.
"""

# Solution

import random

random_list = [random.randint(1, 10) for _ in range(10)]

def draw_histogram(random_list):
    for i in random_list:
        print(i * '@')

draw_histogram(random_list)
