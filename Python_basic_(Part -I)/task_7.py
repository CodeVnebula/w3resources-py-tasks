"""
Write a Python program that accepts a filename from the user and prints the extension of the file.
Sample filename : abc.java
Output : java
"""

# Solution

file_name = input('Enter full filename: ')
extension = file_name.split('.')[-1]
print("Extension: " + extension)
