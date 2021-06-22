# --------------------------------------------------------------
# File:     Week-13-1/gui-7-exercise.py
# Project:  Python-Class-Demos
# Author:   Adrian Gould <Adrian.Gould@nmtafe.wa.edu.au>
# Created:  11/05/2021
# Purpose:  Practice using GUI
#
# Problem:  Create a GUI that asks a user for their name and
#           the year of their birth. When a button is pressed
#           it presents a greeting of the form
#           "Welcome NAME, you are XX this year."
#
#           The GUI should look something like this:
#           Name:           __________________      label/text input
#           Birth Year:     __________________      label/number input
#           __________________________________      label
#                           [How Old?]              button
# --------------------------------------------------------------


from breezypythongui import EasyFrame


class AgeApplication(EasyFrame):
    def __init__(self):
        """Sets up the window, labels, and button."""
        EasyFrame.__init__(self)
        self.setSize(600, 300)
        self.setTitle("How old am I?")

    # Methods to handle user events.



def main():
    """Entry point for the application."""
    AgeApplication().mainloop()


if __name__ == "__main__":
    main()
