# --------------------------------------------------------------
# File:     Week-13-1/gui-6.py
# Project:  Python-Class-Demo
# Author:   Adrian Gould <Adrian.Gould@nmtafe.wa.edu.au>
# Created:  11/05/2021
# Purpose:  Counter with an instance variable
# --------------------------------------------------------------

from breezypythongui import EasyFrame


class CounterApplication(EasyFrame):
    """Illustrates the use of a counter with an
    instance variable."""

    def __init__(self):
        """Sets up the window, label, and buttons."""
        EasyFrame.__init__(self)
        self.setSize(250, 100)
        self.setTitle("Counter Application")

        # Instance variable to track the count.
        self.count = 0

        # A label to display the count in the first row.
        self.counterLabel = self.addLabel(text=self.count,
                                          row=0,
                                          column=0,
                                          sticky="NSEW",
                                          columnspan=2)

        # Two command buttons: Next and Reset
        self.addButton(text="Next",
                       row=1,
                       column=0,
                       command=self.next_count)

        self.addButton(text="Reset",
                       row=1,
                       column=1,
                       command=self.reset_count)

    # Methods to handle user events.
    def next_count(self):
        """Increments the count and updates the display."""
        self.count += 1
        self.counterLabel["text"] = str(self.count)

    def reset_count(self):
        """Resets the count to 0 and updates the display."""
        self.count = 0
        self.counterLabel["text"] = str(self.count)


def main():
    """Entry point for the application."""
    CounterApplication().mainloop()


if __name__ == "__main__":
    main()
