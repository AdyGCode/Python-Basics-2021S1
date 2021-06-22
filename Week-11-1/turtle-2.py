# --------------------------------------------------------------
# File:     Week-11-1/turtle-2.py
# Project:  Python-Class-Demos
# Author:   Adrian Gould <Adrian.Gould@nmtafe.wa.edu.au>
# Created:  27/04/2021
# Purpose:  ...
#
# --------------------------------------------------------------
from time import sleep
from turtle import Turtle


def drawSquare(t, x, y, length):
    t.up()
    t.goto(x, y)
    t.down()
    for count in range(4):
        t.forward(length)
        t.left(90)


def drawSomething(t, x=0, y=0, size=60,
                  angle=360, penColour="#000000"):
    t.pencolor(penColour)
    turns = 360 // angle
    for count in range(turns):
        t.setheading(angle * count)
        drawSquare(t, x, y, size)
    t.hideturtle()


def main():
    t = Turtle()
    drawSomething(t, angle=30, penColour="#999900")
    drawSomething(t, angle=12, x=100, y=100, penColour="#009999")
    drawSomething(t, angle=45, x=-100, y=-100, penColour="#990099")
    sleep(10)


if __name__ == '__main__':
    main()
