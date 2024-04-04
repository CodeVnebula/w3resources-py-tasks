"""
Write a Python program that determines whether a given number (accepted from the user) 
is even or odd, and prints an appropriate message to the user.
"""

# Solution

def even_or_odd(a):
    return 'even' if a % 2 == 0 else 'odd'

a = int(input("Enter number: "))

result = even_or_odd(a)

print(f'{a} is {result} number')
