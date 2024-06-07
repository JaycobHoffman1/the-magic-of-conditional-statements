# Task 1: Identify the Greatest
print('Identify the Greatest')
num1 = int(input('Enter a number: '))
num2 = int(input('Enter a different number: '))
num3 = int(input('Enter a different number: '))

if num1 >= num2 and num1 >= num3:
    largest_num = num1
elif num2 >= num1 and num2 >= num3:
    largest_num = num2
elif num3 >= num1 and num3 >= num2:
    largest_num = num3

print(f'{largest_num} is the largest number!')


# Task 2: Identify the Smallest
print('Identify the Smallest')
num1 = int(input('Enter a number: '))
num2 = int(input('Enter a different number: '))
num3 = int(input('Enter a different number: '))

if num1 >= num2 and num1 >= num3:
    largest_num = num1
elif num2 >= num1 and num2 >= num3:
    largest_num = num2
elif num3 >= num1 and num3 >= num2:
    largest_num = num3

if num1 <= num2 and num1 <= num3:
    smallest_num = num1
elif num2 <= num1 and num2 <= num3:
    smallest_num = num2
elif num3 <= num1 and num3 <= num2:
    smallest_num = num3

print(f'{largest_num} is the largest number and {smallest_num} is the smallest number!')


# Task 3: Equality Check
print('Equality Check')
num1 = int(input('Enter a number: '))
num2 = int(input('Enter another number: '))
num3 = int(input('Enter another number: '))

if num1 >= num2 and num1 >= num3:
    largest_num = num1
elif num2 >= num1 and num2 >= num3:
    largest_num = num2
elif num3 >= num1 and num3 >= num2:
    largest_num = num3

if num1 <= num2 and num1 <= num3:
    smallest_num = num1
elif num2 <= num1 and num2 <= num3:
    smallest_num = num2
elif num3 <= num1 and num3 <= num2:
    smallest_num = num3

if num1 == num2 != num3:
    print(f'{largest_num} is the largest number and {smallest_num} is the smallest number. Two numbers are equal, both are {num1}.')
elif num2 == num3 != num1:
    print(f'{largest_num} is the largest number and {smallest_num} is the smallest number. Two numbers are equal, both are {num2}.')
elif num1 == num3 != num2:
    print(f'{largest_num} is the largest number and {smallest_num} is the smallest number. Two numbers are equal, both are {num3}.')
elif num1 == num2 == num3:
    print('All numbers are equal!')
