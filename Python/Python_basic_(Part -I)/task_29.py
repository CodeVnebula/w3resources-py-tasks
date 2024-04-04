"""
Write a Python program that prints out all colors from color_list_1 that are not present in color_list_2.
Test Data :
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
Expected Output :
{'Black', 'White'}
"""

# Solution

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

def not_in_list(list_1, list_2):
    print(list_1.difference(list_2))

not_in_list(color_list_1, color_list_2)
            