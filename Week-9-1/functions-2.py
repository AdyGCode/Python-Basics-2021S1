# --------------------------------------------------------------
# File:     Week-9-1/functions-2.py
# Project:  Python-Class-Demos
# Author:   Adrian Gould <Adrian.Gould@nmtafe.wa.edu.au>
# Created:  13/04/2021
# Purpose:  ...
#
# --------------------------------------------------------------

number_counts = {
    1: 10,
    2: 9,
    3: 9,
    4: 10,
    5: 8
}

mode_numbers = []
biggest = max(number_counts.values())
for key in number_counts:
    if number_counts[key] == biggest:
        mode_numbers.append(key)

print(mode_numbers)
