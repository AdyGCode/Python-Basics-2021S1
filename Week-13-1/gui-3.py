# --------------------------------------------------------------
# File:     Week-13-1/gui-3.py
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

        # A single label in the first row.
        self.label = self.addLabel(text="Hello world!",
                                   row=0,
                                   column=0,
                                   columnspan=2,
                                   sticky="NSEW")

        # Two command buttons in the second row.
        self.clearBtn = self.addButton(text="Clear",
                                       row=1,
                                       column=0,
                                       command=self.clear)

        self.restoreBtn = self.addButton(text="Restore",
                                         row=1,
                                         column=1,
                                         command=self.restore,
                                         state="disabled")

    # Definitions of event handling methods
    def clear(self):
        """Resets the label to the empty string and the button states."""
        self.label["text"] = ""
        self.clearBtn["state"] = "disabled"
        self.restoreBtn["state"] = "normal"

    def restore(self):
        """Resets the label to 'Hello world!'and sets
        the state of the buttons."""
        self.label["text"] = "Hello world!"
        self.clearBtn["state"] = "normal"
        self.restoreBtn["state"] = "disabled"


def main():
    ApplicationName().mainloop()


if __name__ == "__main__":
    main()
