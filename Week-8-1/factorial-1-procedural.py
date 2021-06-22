"""
File:       Week-8-1/factorial-1-procedural.py
Author:     Adrian Gould
Purpose:    Demonstrate the use of procedural code to calculate the
            factorial of a number

Design:
    Define factorial function
        result is 1
        if number > 1
            for count in range 1 to number
                result is result time number
            end for
        end if
        return number

    Define main function
        ask user for an integer
        calculate the factorial number
        display the result

    If main is being executed:
        call main function

Test:
    number          results
        0               1
        1               1
        2               2
        3               6

"""


def factorial(number):
    result = 1
    if number > 1:
        for count in range(1, number + 1):
            result *= count  # result = result * count
    return result

def factorial_shorter(number):
    """ Calculate the factorial of an integer

    This is the shorter version of the factorial (no if)
    :param number: integer
    :return: integer
    """
    result = 1
    for count in range(1, number + 1):
        result *= count  # result = result * count
    return result

def main():
    number = int(input("Enter an integer: "))
    fact = factorial(number)
    print(f"{number}! is {fact}")


if __name__ == "__main__":  # dunder __ (two consecutive underscores)
    main()
