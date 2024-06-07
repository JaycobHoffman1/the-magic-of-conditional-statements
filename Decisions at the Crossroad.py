# Task 1: Code Correction
'''
Buggy Code
----------------------------------
number = input("Enter a number: ")

if number > 0:
    print("The number is positive.")
elif number = 0:
    print("The number is zero.")
else number < 0:
    print("The number is negative.")
'''

# Corrected code:
number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number == 0:
    print("The number is zero.")
elif number < 0:
    print("The number is negative.")