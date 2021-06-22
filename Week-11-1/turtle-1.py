"""
File:     Week-11-1/turtle-1.py
Author:   Adrian Gould
Purpose:  Fun with the turtle:
          Draw a square

Design:   n/a

Requires: turtle
"""

import turtle
import time


def drawSquare(t, x, y, length):
    """Draw a square with a turtle

	Draws a square with the given turtle t, an upper-left
	corner point (x, y), and a side's length.

    :param t: turtle
    :param x: integer x-axis position (top-left)
    :param y: integer y-axis position
    :param length: integer length of sides
    :return:
    """
    t.up()
    t.goto(x, y)
    t.setheading(270)
    t.down()
    for count in range(4):
        t.forward(length)
        t.left(90)
    t.setheading(0)


def drawRectangle(t, x, y, length, width):
    t.up()
    t.goto(x, y)
    t.setheading(270)
    t.down()
    for count in range(2):
        t.forward(length)
        t.left(90)
        t.forward(width)
        t.left(90)
    t.setheading(0)

def drawTriangle(t, x,y, length):
    t.up()
    t.goto(x, y)
    t.setheading(180)
    t.down()
    for count in range(3):
        t.right(120)
        t.forward(length)
    t.setheading(0)


def main():
    # instantiate (create) a Turtle object
    t = turtle.Turtle()  # turtle = package, Turtle = class
    drawSquare(t, 20, 40, 60)
    drawRectangle(t, -100, 0, 60, 100)
    drawTriangle(t, 100, -50, 60)
    time.sleep(5)


if __name__ == "__main__":
    main()
