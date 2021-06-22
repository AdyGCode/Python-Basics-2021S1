# File:     Week-4-1/fizz-buzz.py
# Author:   Adrian Gould
# Purpose:  Have Python play Fizz-Buzz by itself


# Ask user for the maximum number to go to...
max_number = None
while max_number is None or max_number <= 0:
    try:
        max_number = int(input("Enter the maximum number:"))
        if max_number <= 0:
            print("ERROR: Number must be an integer greater than 0")
    except ValueError:
        print("ERROR: Number must be a positive integer")
        max_number = None

number = 1
while number <= max_number:
    output = ""
    if number % 2 == 0:
        output = output + "fizz "
    if number % 3 == 0:
        output += "buzz"
    if number % 2 != 0 and number % 3 != 0:
        output = number
    print(f"{number:>3} {output}")
    number += 1
