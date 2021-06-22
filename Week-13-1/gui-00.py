# --------------------------------------------------------------
# File:     Week-13-1/gui-00.py
# Project:  Python-Class-Demo
# Author:   Adrian Gould <Adrian.Gould@nmtafe.wa.edu.au>
# Created:  11/05/2021
# Purpose: Base Code
# --------------------------------------------------------------
from breezypythongui import EasyFrame


class ApplicationName(EasyFrame):
    """Demonstrates the use of prompter boxes."""

    def __init__(self):
        """Sets up the window and widgets."""
        EasyFrame.__init__(self,
                           title="Guessing Game",
                           width=300,
                           height=300,
                           background="#f3f3f3")
        # Add the widgets after this
        self.aLabel = self.addLabel(text="A Label",
                                    row=1,
                                    column=0,
                                    columnspan=2,
                                    sticky="EW",
                                    font="Verdana")

    # Command handling methods are added after this
    def command_method(self):
        # create the method code here
        # delete pass when adding code
        pass


def main():
    """Instantiate and pop up the window."""
    ApplicationName().mainloop()


if __name__ == "__main__":
    main()
