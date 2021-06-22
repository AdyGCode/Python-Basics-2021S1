# --------------------------------------------------------------
# File:     Week-11-1/turtle-4.py
# Project:  Python-Class-Demos
# Author:   Adrian Gould <Adrian.Gould@nmtafe.wa.edu.au>
# Created:  27/04/2021
# Purpose:  ...
#
# --------------------------------------------------------------
from time import sleep
from turtle import Turtle

import random


def randomWalk(t, turns, distance=20):
    """Turns a random number of degrees and moves a given
    distance for a fixed number of turns."""
    for x in range(turns):
        if x % 2 == 0:
            t.left(random.randint(-180, 180))
        else:
            t.right(random.randint(-180, 180))
        t.forward(random.randint(1,distance))
    sleep(10)

def main():
    t = Turtle()
    t.shape("turtle")
    randomWalk(t, 40, 100)


if __name__ == '__main__':
    main()
