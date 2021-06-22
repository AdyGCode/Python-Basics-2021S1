"""
File:       Week-8-1/data-entry-bonus.py
Author:     Adrian Gould
Purpose:    Demonstrate how to create a routine to ask for an unknown
            quantity of numbers and then add them to a list. The data
            entry is ended when a letter Q or q is submitted. Other
            entries are rejected if not an integer.

Design:
    numbers is empty list
    finished is false
    while not finished
        ask for a next value
        if the value is a Q then
            finished is true
        else
            (Need to capture and handle any exception)
            value is integer value
            append value to numbers list

"""
numbers = []
finished = False
while not finished:
    value = input("Enter a whole number (Q to finish):")
    if value.upper() == "Q":
        finished = True
    else:
        try:
            value = int(value)
            numbers.append(value)
        except ValueError:
            value = None
            print("Please enter an integer, or Q to finish")

print(numbers)
