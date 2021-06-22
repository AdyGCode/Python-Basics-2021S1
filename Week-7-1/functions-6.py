"""
File:       Week-7-1/functions-6.py
Author:     Adrian Gould
Purpose:    Demonstrate taking code and making it a function
            This builds on the functions 5 code and adds the ability
            to provide a 'coder defined' prompt and minimum and
            maximum values that may be entered

Design:
    Define get_integer function (with prompt, maximum and minimum)
        Define number to be None
        While number is none and number not between minimum and
                    maximum inclusive
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


def get_integer(minimum=1, maximum=10, prompt="Enter an integer:"):
    number = None
    while number is None and number not in range(minimum, maximum + 1):
        try:
            number = int(input(prompt))
            break  # cheat - let's get outta the loop NOW!
        except ValueError:
            print(f"OOPS! Please enter a value in the range {minimum} "
                  f"to {maximum}...")
    return number


def main():
    number1 = get_integer()
    number2 = get_integer(10, 50)
    number3 = get_integer(minimum=100, maximum=500)
    number4 = get_integer(1, 5, "Enter a choice (1-5)")
    number5 = get_integer(minimum=1, maximum=5,
                          prompt="Enter a choice (1-5)")
    number6 = get_integer(prompt="Enter a number", minimum=1, maximum=5)
    age = get_integer(0, 150, "Enter your age in years: ")

    print(f"Number 1:    {number1}")
    print(f"Number 2:    {number2}")
    print(f"Number 3:    {number3}")
    print(f"Number 4:    {number4}")
    print(f"Number 5:    {number5}")
    print(f"Number 6:    {number6}")
    print(f"Your age is: {age}")


if __name__ == "__main__":
    main()
