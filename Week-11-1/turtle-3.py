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
    t.screen.bgcolor("orange")
    x = t.screen.window_width() // 2
    y = t.screen.window_height() // 2
    print(f"Screen Size: {x*2}, {y*2}")
    print(f"Top Left: ({-x}, {y})")
    print(f"Bottom Right: ({x}, {-y})")
    sleep(10)


if __name__ == '__main__':
    main()
