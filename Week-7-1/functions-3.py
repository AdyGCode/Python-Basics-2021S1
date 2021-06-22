"""
File:       Week-7-1/functions-3.py
Author:     Adrian Gould
Purpose:    Demonstrate taking code and making it a function
            This version has a problem when a decimal or non integer
            is entered... an error will be displayed and it will ask
            again. If the value entered is an integer then it will
            display the value.

Design:
    Define main function
        Define number to be None
        While number is none
            Try the following
                Ask user for an integer
                Break from While loop
            If an exception given:
                Display "Ooops! Not an integer"
        Display the number

    If main is being executed:
        Call main function

Test:
    Run code and enter the following value: 123
    Run code and enter the following value: 12.5
    Run code and enter the following value: abc
"""


def main():
    number = None
    while number is None:
        try:
            number = int(input("Enter an integer: "))
            break  # cheat - let's get outta the loop NOW!
        except ValueError:
            print("OOPS! not an integer value")

    number1 = number

    print(number1)


if __name__ == "__main__":
    main()
