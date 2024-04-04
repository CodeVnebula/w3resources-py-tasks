"""
43. Write a Python program to get OS name, platform and release information. 

Link: https://www.w3resource.com/python-exercises/python-basic-exercise-43.php
"""

# Solution

import os
import platform

print(os.name)
print(platform.system())
print(platform.release())
