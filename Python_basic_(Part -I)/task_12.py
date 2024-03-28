"""
Write a Python program that prints the calendar for a given month and year.
Note : Use 'calendar' module.
"""

# Solution
import calendar

month = int(input("Enter month: "))
year = int(int(input("Enter year: ")))

print(calendar.month(year, month))
