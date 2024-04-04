"""
Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
Sample value of n is 5
Expected Result : 615
"""

# Solution

number = int(input("Enter an integer: "))

n = int('%s' % number)                      # %s used for formating a string
nn = int('%s%s' % (number, number))
nnn = int('%s%s%s' % (number, number, number))
_sum = n + nn + nnn
print('n + nn + nnn = ', _sum)
