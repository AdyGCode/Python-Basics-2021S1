# --------------------------------------------------------------
# File:     Week-13-1/gui-10.py
# Project:  Python-Class-Demo
# Author:   Adrian Gould <Adrian.Gould@nmtafe.wa.edu.au>
# Created:  11/05/2021
# Purpose:  Panels and layouts
# --------------------------------------------------------------


from breezypythongui import EasyFrame


class LayoutsWithPanels(EasyFrame):

    def __init__(self):
        # Create the main frame
        EasyFrame.__init__(self,
                           title="Panel Demo - v2")

        # Create the panel for the data
        dataPanel = self.addPanel(row=0,
                                  column=0,
                                  background="gray")

        # Create and add widgets to the data panel
        dataPanel.addLabel(text="Label 1",
                           row=0,
                           column=0,
                           background="purple",
                           foreground="white")

        dataPanel.addTextField(text="Text1",
                               row=0,
                               column=1)

        dataPanel.addLabel(text="Label 2",
                           row=1,
                           column=0,
                           background="pink")

        dataPanel.addTextField(text="Text2",
                               row=1,
                               column=1)

        # Create the nested frame for the button panel
        buttonPanel = self.addPanel(row=1,
                                    column=0,
                                    background="green")

        # Create and add buttons to the button panel
        buttonPanel.addButton(text="Button 1",
                              row=0,
                              column=0)

        buttonPanel.addButton(text="Button 2",
                              row=0,
                              column=1)

        buttonPanel.addButton(text="Another Button",
                              row=0,
                              column=2)


def main():
    """Instantiate and pop up the window."""
    LayoutsWithPanels().mainloop()


if __name__ == "__main__":
    main()
