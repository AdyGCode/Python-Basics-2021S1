# --------------------------------------------------------------
# File:     Week-11-1/turtle-6.py
# Project:  Python-Class-Demos
# Author:   Adrian Gould <Adrian.Gould@nmtafe.wa.edu.au>
# Created:  27/04/2021
# Purpose:
#
# --------------------------------------------------------------
from time import sleep
from turtle import Turtle

import random


def main():
    t = Turtle()
    t.speed(1)
    t.up()
    name = "Adrian"
    turns = 6
    angle = 360 // turns
    for count in range(0, turns):
        t.write(name)
        t.left(angle)
        t.forward(50)
    sleep(10)


if __name__ == "__main__":
    main()
