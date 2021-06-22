# --------------------------------------------------------------
# File:     Week-13-1/gui-1.py
# Project:  Python-Class-Demos
# Author:   Adrian Gould <Adrian.Gould@nmtafe.wa.edu.au>
# Created:  11/05/2021
# Purpose:  Demonstrate GUI concepts
#
# Preparation:
#   Create a new folder Week-13-1
#   Create a new folder Samples inside Week-13-1
#   Download the following from Blackboard:
#       Chapter 8 Student Sample Data Files (Session 13)
#   Uncompress the files from the compressed file
#   Copy the files into the Samples folder
#   Copy the breezypythongui.py file into the Week-13-1 folder
# --------------------------------------------------------------

# The brezypythongui and EasyFrame will be red squiggly underlined
from breezypythongui import EasyFrame


# Create a new class and INHERIT the EasyFrame capabilities
class ApplicationName(EasyFrame):
    # The __init__ method definition
    def __init__(self):
        """
        Sets up the window and the label.
        """
        EasyFrame.__init__(self,
                           width=300,
                           height=200,
                           title="Label Demo")

        self.addLabel(text="Hello world!",
                      row=0,
                      column=0)

        # Definitions of event handling methods


def main():
    ApplicationName().mainloop()


if __name__ == "__main__":
    main()
