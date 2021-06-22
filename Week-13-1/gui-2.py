# --------------------------------------------------------------
# File:     Week-13-1/gui-2.py
# Project:  Python-Class-Demos
# Author:   Adrian Gould <Adrian.Gould@nmtafe.wa.edu.au>
# Created:  11/05/2021
# Purpose:  Demonstrate GUI concepts
#
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

        self.addLabel(text="(0, 0)",
                      row=0,
                      column=0,
                      sticky="NSEW")
        self.addLabel(text="(0, 1)",
                      row=0,
                      column=1,
                      sticky="NEWS")
        self.addLabel(text="(1, 0)",
                      row=1,
                      column=0,
                      sticky="NESW")
        self.addLabel(text="(1, 1) ",
                      row=1,
                      column=1,
                      sticky="WENS")


        # Definitions of event handling methods


def main():
    ApplicationName().mainloop()


if __name__ == "__main__":
    main()
