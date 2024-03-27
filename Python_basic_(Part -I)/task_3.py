"""
    Write a Python program to display the current date and time.
    Sample Output :
    Current date and time :
    2014-07-05 14:34:14
"""

# Solution

from datetime import date, datetime

date = date.today()
now = datetime.now()
current_time = now.strftime('%H:%M:%S')

print(f"Today is: {date} \nTime: {current_time}")
