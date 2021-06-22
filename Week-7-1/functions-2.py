"""
File:       Week-7-1/functions-2.py
Author:     Adrian Gould
Purpose:    Demonstrate taking code and making it a function
            This version has a problem when a decimal or non integer
            is entered... it now will display an error and then stop

Design:
    Define main function
        Try the following
            Ask user for an integer
        If an exception given:
            Display "Ooops! Not an integer"
        Display the number

    If main is being executed:
        call main function

Test:
    Run code and enter the following value: 123
    Run code and enter the following value: 12.5
    Run code and enter the following value: abc
"""



def main():
    try:
        number = int(input("Enter an integer: "))
    except ValueError:
        print("OOPS! not an integer value")

    number1 = number

    print(number1)


if __name__ == "__main__":
    main()
