# --------------------------------------------------------------
# File:     Week-14-1/gui-input-only-letters.py
# Project:  Python-Class-Demos
# Author:   Adrian Gould <Adrian.Gould@nmtafe.wa.edu.au>
# Created:  18/05/2021
# Purpose:  ...
#
# --------------------------------------------------------------


from breezypythongui import EasyFrame
import string


class InputOnlyLetters(EasyFrame):
    """Demonstrate filtering input using keypresses

    Inherits the EasyFrame methods and properties
    """

    def __init__(self):
        """Initialise the frame and instance variables
        """

        self.the_letters = ""

        super().__init__(title="Filtered Input",
                         width=300,
                         height=100)

        # Create the interface
        self.InitialsText = self.addTextField(text="",
                                              row=0,
                                              column=1)

        self.MessageLabel = self.addLabel(text="...",
                                          row=1,
                                          column=1)

        self.InitialsLabel = self.addLabel(text="Initials",
                                           row=0,
                                           column=0,
                                           foreground="#090909")

        self.InitialsText.bind("<Return>",
                               lambda event: self.filter_initials(
                                   event))

    def filter_initials(self, event):
        initials_text = self.InitialsText.getText().upper()
        allowed = string.ascii_uppercase + "*"
        initials = ""
        for letter in initials_text:
            if letter in allowed:
                initials += letter
        self.MessageLabel["text"] = initials[:3]


def main():
    """Instantiate and pop up the window."""
    InputOnlyLetters().mainloop()


if __name__ == "__main__":
    main()
