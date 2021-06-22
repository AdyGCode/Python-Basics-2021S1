# --------------------------------------------------------------
# File:     Week-13-1/gui-9.py
# Project:  Python-Class-Demo
# Author:   Adrian Gould <Adrian.Gould@nmtafe.wa.edu.au>
# Created:  11/05/2021
# Purpose:  Check Boxes
# --------------------------------------------------------------


from breezypythongui import EasyFrame


class CheckboxApplication(EasyFrame):
    """Allows the user to place a restaurant order from a set
    of options."""

    def __init__(self):
        """Sets up the window and widgets."""
        EasyFrame.__init__(self, "Checkbox App")

        # Add four check buttons
        self.chickCheckbox = self.addCheckbutton(text="Chicken",
                                                 row=0,
                                                 column=0)

        self.friesCheckbox = self.addCheckbutton(text="French fries",
                                                 row=0,
                                                 column=1)

        self.beanCheckbox = self.addCheckbutton(text="Baked beans",
                                                row=1,
                                                column=0)

        self.gravyCheckbox = self.addCheckbutton(text="Chicken Gravy",
                                                 row=1,
                                                 column=1)

        self.addButton(text="Place order",
                       row=2,
                       column=0,
                       columnspan=2,
                       command=self.placeOrder)

    # Event handler method

    def placeOrder(self):
        """Display a message box with the order information."""
        message = ""
        if self.chickCheckbox.isChecked():
            message += "Chicken\n\n"
        if self.friesCheckbox.isChecked():
            message += "French fries\n\n"
        if self.beanCheckbox.isChecked():
            message += "Baked beans\n\n"
        if self.gravyCheckbox.isChecked():
            message += "Gravy\n"
        if message == "": message = "No food ordered!"

        self.messageBox(title="Customer Order", message=message)


def main():
    """Instantiate and pop up the window."""
    CheckboxApplication().mainloop()


if __name__ == "__main__":
    main()
