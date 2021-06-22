# --------------------------------------------------------------
# File:     Week-13-1/gui-11.py
# Project:  Python-Class-Demo
# Author:   Adrian Gould <Adrian.Gould@nmtafe.wa.edu.au>
# Created:  11/05/2021
# Purpose:  Prompts
# --------------------------------------------------------------
from breezypythongui import EasyFrame


class PromptTheUser(EasyFrame):
    """Demonstrates the use of prompter boxes."""

    def __init__(self):
        """Sets up the window and widgets."""
        EasyFrame.__init__(self,
                           title="Prompt the User",
                           width=300,
                           height=100)

        # This label will have Verdana as the font
        self.label = self.addLabel(text="",
                                   row=0,
                                   column=0,
                                   sticky="NSEW",
                                   font="Verdana")

        self.addButton(text="Username",
                       row=1,
                       column=0,
                       command=self.getUserName)

    def getUserName(self):
        text = self.prompterBox(title="Enter your User name",
                                promptString="Your username:")
        self.label["text"] = "Hi, " + text + "!"


def main():
    """Instantiate and pop up the window."""
    PromptTheUser().mainloop()


if __name__ == "__main__":
    main()
