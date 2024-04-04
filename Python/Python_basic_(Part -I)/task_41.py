"""
41. Write a Python program to check whether a file exists. 

Link: https://www.w3resource.com/python-exercises/python-basic-exercise-41.php
"""

# Solution

import os

file_name = input("Enter file name with its extension: ")

if not os.path.exists(file_name):
    print(f"File {file_name} doesn't exist")
else:
    print(f"File {file_name} exists")
    