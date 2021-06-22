"""
File:       Week-7-1/functions-1.py
Author:     Adrian Gould
Purpose:    Demonstrate taking code and making it a function
            This version has a problem when a decimal or non integer
            is entered... it will break with an exception

Design:
    Define main function
        Ask user for an integer
        Display the number

    If main is being executed:
        call main function

Test:
    Run code and enter the following value: 123
    Run code and enter the following value: 12.5
    Run code and enter the following value: abc
"""


def main():
    number = int(input("Enter an integer: "))

    # we will use this later...
    number1 = number

    print(number1)


if __name__ == "__main__":
    main()
