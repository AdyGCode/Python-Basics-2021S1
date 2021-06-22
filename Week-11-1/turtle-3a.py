# --------------------------------------------------------------
# File:     Week-11-1/turtle-3.py
# Project:  Python-Class-Demos
# Author:   Adrian Gould <Adrian.Gould@nmtafe.wa.edu.au>
# Created:  27/04/2021
# Purpose:  ...
#
# --------------------------------------------------------------
from time import sleep
from turtle import Turtle


def main():
    t = Turtle()
    for r in range(0, 256, 4):
        for g in range(0, 256, 4):
            for b in range(0, 256, 4):
                c = r * 16 * 16 + g * 16 + b
                t.screen.bgcolor(f"#{c:06x}")


if __name__ == '__main__':
    main()
