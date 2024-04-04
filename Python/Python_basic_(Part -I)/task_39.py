"""
39. Write a Python program to compute the future value of a specified principal amount, rate of interest, and number of years. 
Test Data : amt = 10000, int = 3.5, years = 7
Expected Output : 12722.79

Link: https://www.w3resource.com/python-exercises/python-basic-exercise-39.php

The formula for future value with compound interest is future_value = amt * (1 + int)^years.
"""

# Solution

amt = 10000
int = 3.5
years = 7

future_value = amt * ((1 + (0.01 * int)) ** years)
print(round(future_value, 2))
