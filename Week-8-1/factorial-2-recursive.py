"""
File:       Week-8-1/factorial-1-recursive.py
Author:     Adrian Gould
Purpose:    Demonstrate the use of recursive code to calculate the
            factorial of a number

Design:
    Define factorial function
        if number > 1
            return number times factorial (number - 1)
        end if
        return 1

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
    if number > 1:
        return number * factorial(number - 1)
    return 1

"""
number      factorial(n)
    4           4 * factorial(3)
                    3 * factorial(2)
                        2 * factorial(1)
                            1
                        2 * 1
                    3 * 2
                4 * 6
                24
"""


def main():
    number = int(input("Enter an integer: "))
    fact = factorial(number)
    print(f"{number}! is {fact}")


if __name__ == "__main__":
    main()
