"""
File:       Week-7-1/functions-5.py
Author:     Adrian Gould
Purpose:    Demonstrate taking code and making it a function
            This builds on the functions 4 code and adds the ability
            to provide a 'coder defined' prompt.

Design:
    Define get_integer function (with prompt)
        Define number to be None
        While number is none
            Try the following
                Ask user for an integer
                Break from While loop
            If an exception given:
                Display "Ooops! Not an integer"
        return number

    Define main function
        number1 is get integer ("enter your age")
        Display the number

    If main is being executed:
        Call main function

Test:
    Run code and enter the following value: 123
    Run code and enter the following value: 12.5
    Run code and enter the following value: abc
"""


def get_integer(prompt="Enter an integer:"):
    number = None
    while number is None:
        try:
            number = int(input(prompt))
            break  # cheat - let's get outta the loop NOW!
        except ValueError:
            print("OOPS! not an integer value")
    return number


def main():
    number1 = get_integer()
    age = get_integer("Enter your age in years: ")

    print(f"Number 1:    {number1}")
    print(f"Your age is: {age}")


if __name__ == "__main__":
    main()
