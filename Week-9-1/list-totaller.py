# --------------------------------------------------------------
# File:     Week-9-1/list-totaller.py
# Project:  Python-Class-Demos
# Author:   Adrian Gould <Adrian.Gould@nmtafe.wa.edu.au>
# Created:  13/04/2021
# Purpose:  Demonstrate variable scope
#
# --------------------------------------------------------------
numbers = [7, 6, 1, 3, 17, 21]
the_total = None


def total(number_list=[]):
    the_total = 0  # NOT the same variable as the_total defined above
    print(the_total)
    for number in number_list:
        the_total += number
    print(the_total)
    return the_total


print(f"Before totalling: {the_total}")
the_total = total(numbers)
print(f"After totalling : {the_total}")
