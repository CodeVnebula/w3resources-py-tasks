"""
Write a Python program to test whether a passed letter is a vowel or not.
"""

# Solution

VOV_LETTERS = 'aeiou'

def check_vovel(letter):
    return True if letter.lower() in VOV_LETTERS else False

letter = input("Enter a single letter: ")
while len(letter) > 1 or not letter.isalpha():
    letter = input("Error! PLease enter only one non-numeric character: ")

result = 'vovel' if check_vovel(letter) else 'consonant'

print(f'"{letter}" is {result}')
