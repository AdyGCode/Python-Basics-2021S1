# --------------------------------------------------------------
# File:     Week-11-1/turtle-5.py
# Project:  Python-Class-Demos
# Author:   Adrian Gould <Adrian.Gould@nmtafe.wa.edu.au>
# Created:  27/04/2021
# Purpose:  Draws a radial pattern of squares in a random fill
#           color at each corner of the window.
#
# Requires: polygons
#           CTRL+ALT+S (Properties, CMD+, on Mac)
#           Project --> Project Interpreter --> + (on right)
#           Search for polygons in packages, Install
#           Close window, click OK
# --------------------------------------------------------------
from time import sleep
from turtle import Turtle

import random
from polygons import *


def radialPattern(t, n, length, shape):
    """Draws a radial pattern of n shapes with the given length."""
    for count in range(n):
        shape(t, length)
        t.left(360 / n)


def drawPattern(t, x, y, count, length, shape):
    """Draws a radial pattern with a random
    fill color at the given position."""
    t.begin_fill()
    t.up()
    t.goto(x, y)
    t.setheading(0)
    t.down()
    t.fillcolor(random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255))
    radialPattern(t, count, length, shape)
    t.end_fill()


def main():
    t = Turtle()
    t.speed(0)
    # Number of shapes in radial pattern
    count = 10
    # Relative distances to corners of window from center
    width = t.screen.window_width() // 2
    height = t.screen.window_height() // 2
    # Length of the square
    length = 30
    # Inset distance from window boundary for squares
    inset = length * 2
    # Draw squares in upper-left corner
    drawPattern(t, -width + inset, height - inset, count,
                length, square)
    # Draw squares in lower-left corner
    drawPattern(t, -width + inset, inset - height, count,
                length, square)
    # Length of the hexagon
    length = 20
    # Inset distance from window boundary for hexagons
    inset = length * 3
    # Draw hexagons in upper-right corner
    drawPattern(t, width - inset, height - inset, count,
                length, hexagon)
    # Draw hexagons in lower-right corner
    drawPattern(t, width - inset, inset - height, count,
                length, hexagon)


if __name__ == "__main__":
    main()
