"""
File:       Week-7-1/functions-4.py
Author:     Adrian Gould
Purpose:    Demonstrate taking code and making it a function
            Move the get integer code to a function (see functions-3
            for the previous code)

Design:
    Define get_integer function
        Define number to be None
        While number is none
            Try the following
                Ask user for an integer
                Break from While loop
            If an exception given:
                Display "Ooops! Not an integer"
        return number

    Define main function
        Define number1 as the result from "get integer"
        Display the number

    If main is being executed:
        Call main function

Test:
    Run code and enter the following value: 123
    Run code and enter the following value: 12.5
    Run code and enter the following value: abc
"""



def get_integer():
    number = None
    while number is None:
        try:
            number = int(input("Enter an integer: "))
            break  # cheat - let's get outta the loop NOW!
        except ValueError:
            print("OOPS! not an integer value")
    return number


def main():
    number1 = get_integer()

    print(number1)


if __name__ == "__main__":
    main()
