"""
Write a Python program to calculate the number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days
"""

# Solution

from datetime import date

date_one = date(2014, 7, 2)
date_two = date(2014, 7, 11)

delta = date_two - date_one

print(abs(delta.days), "days")
