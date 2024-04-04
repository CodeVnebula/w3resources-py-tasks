"""
Write a Python program that displays your name, age, and address on three different lines.
"""

# Solution

def print_details(name: str, age: int, address: str):
  #  print(f"DETAILS:\nName: {name} \nAge: {age} \nAddress: {address}")
    print("DETAILS:\nName: {}\nAge: {}\nAddress: {}".format(name, age, address))

print_details("Alice", 19, "123 Main Street")
