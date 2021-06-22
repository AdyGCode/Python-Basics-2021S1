# --------------------------------------------------------------
# File:     Week-12-1/main.py
# Project:  Python-Class-Demos
# Author:   Adrian Gould <Adrian.Gould@nmtafe.wa.edu.au>
# Created:  4/05/2021
# Purpose:  Demonstrate using the MiniFig class
#
# --------------------------------------------------------------

from Head import MiniFig, Head, Body, Legs


def main():
    print(
        "Note how we do not get the test results from the Head.py file")
    elsa = MiniFig(name="Elsa")
    elsa.head = Head(colour="peach")
    print(elsa)

if __name__ == "__main__":
    main()
