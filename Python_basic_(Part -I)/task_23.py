"""
Write a Python program to get n (non-negative integer) copies of the first 2 characters 
of a given string. Return n copies of the whole string if the length is less than 2.
"""

# Solution

def make_copies(string, n):
    string_copy = ''
    for _ in range(n):
        string_copy += string[:2]
    return string_copy

n = int(input("Enter n (n > 0): "))
 
while n <= 0:
    n = int(input("Please enter non-negative n: "))

string = input("Enter string: ")

result = (n * string) if n < 2 else make_copies(string, n)

print("Result: ", result)
