"""
Write a Python program to get a newly-generated string from a given string where "Is" has 
been added to the front. Return the string unchanged if the given string already begins with "Is".
"""

# Solution

def new_string(string):
    if len(string) >= 2 and string.lower().startswith('is'):
        return string
    else:
        return 'Is ' + string

string = input('Enter string: ')

print('Generated string: ', new_string(string))
