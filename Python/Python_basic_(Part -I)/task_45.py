"""
45.  Write a Python program that calls an external command. 

Link: https://www.w3resource.com/python-exercises/python-basic-exercise-45.php
"""

# Solution

from subprocess import call

call(["cmd.exe", "/c", "dir"])
