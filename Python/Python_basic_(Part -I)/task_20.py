"""
Write a Python program that returns a string that is n (non-negative integer) copies of a given string.
"""

# Solution

def string_copies(string, n):
    new_string = ''
    for _ in range(n):
        new_string += string
    return new_string

# Call the function
n = int(input("Enter n (n > 0): "))
 
while n <= 0:
    n = int(input("Please enter non-negative n: "))

string = input("Enter string: ")
result = string_copies(string, n)
print(result)
