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
    t.write("Hello")
    t.goto(0,100)
    t.write("Hello",font=("Trebuchet", 10, "bold"))
    t.goto(0,-100)
    t.pencolor("#990000")
    t.write("Hello",font=("Verdana", 12, "normal"), move=True)
    sleep(5)


if __name__ == "__main__":
    main()
