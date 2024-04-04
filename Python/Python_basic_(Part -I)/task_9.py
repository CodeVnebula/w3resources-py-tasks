"""
Write a Python program to display the examination schedule. (extract the date from exam_st_date).
exam_st_date = (11, 12, 2014)
Sample Output : The examination will start from : 11 / 12 / 2014
"""

# Solution

exam_st_date = (11, 12, 2014)
day = exam_st_date[0]
month = exam_st_date[1]
year = exam_st_date[-1]

print('The examination will start from: ' + str(day) + '/' + str(month) + '/' + str(year))
