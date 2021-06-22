# --------------------------------------------------------------
# File:     Week-13-2/gui-2-guessing-game.py
# Project:  Python-Class-Demos
# Author:   Adrian Gould <Adrian.Gould@nmtafe.wa.edu.au>
# Created:  13/05/2021
# Purpose:  GUI Guessing Game version 2
#
# Duplicate the first version of the guessing game.
#
# You will enhance this version of the game by:
#   1) When the computer gives a general message the text will be
#   black on a white background
#   2) When the user guesses too high, the computer will display the
#   "too high" message in white text on a red background
#   3) When the user guesses too low, the computer will display the
#   "too low" message in white text on a blue background
#   4) When the user guesses correctly, the computer will display the
#   congratulations message in white text on a green background
# --------------------------------------------------------------

from random import randint

from breezypythongui import EasyFrame


class GuessingGame(EasyFrame):
    """Guessing Game Class

    Inherits the EasyFrame methods and properties
    """

    def __init__(self):
        """Initialise the frame and instance variables

            count               integer counts the guesses
            computer_number     a random number for the user to guess
            message             the message to
        """
        self.count = 0
        self.computer_number = randint(1, 100)
        self.computer_number = 50
        self.message = ""
        self.fg = "#000000"
        self.bg = "#000000"
        self.scores = []

        super().__init__(title="Guessing Game",
                         width=300)

        # EasyFrame.__init__(self,
        #                    title="Guessing Game",
        #                    width=300,
        #                    height=150)
        #
        # Create the interface
        self.Title = self.addLabel(text="Guess the Number",
                                   row=0,
                                   column=0,
                                   columnspan=3,
                                   sticky="EW",
                                   font="Verdana",
                                   foreground="#ffffff",
                                   background="#000000")

        self.GuessLabel = self.addLabel(text="What is your Guess?",
                                        row=1,
                                        column=0,
                                        foreground="#090909")

        self.NumberGuessed = self.addIntegerField(value=0,
                                                  row=1,
                                                  column=1)

        self.GuessButton = self.addButton(text="Guess!",
                                          row=1,
                                          column=2,
                                          command=self.check_guess)

        self.MessageLabel = self.addLabel(text="take a guess..",
                                          row=2,
                                          column=0,
                                          columnspan=3,
                                          sticky="EW")

    # Command handling methods are added after this
    def check_guess(self):
        # create the method code here
        # delete pass when adding code
        try:
            user_number = self.NumberGuessed.getNumber()
            self.count += 1
            self.fg = "#000000"
            self.bg = "#ffffff"
            if user_number > self.computer_number:
                self.message = "Too High!"
                self.bg = "#ff0000"
                self.fg = "#ffffff"
            elif user_number < self.computer_number:
                self.message = "Too Low!"
                self.bg = "#0000ff"
                self.fg = "#ffffff"
            else:
                self.message = f"You got it in {self.count} guesses!"
                self.bg = "#00ff00"
                self.fg = "#ffffff"
                # self.show_high_scores()
                # self.quit()

        except ValueError:
            self.message = "You need to enter an integer"
            self.bg = "#ffbb00"
            self.fg = "#000000"

        finally:
            self.MessageLabel["text"] = self.message
            self.MessageLabel["foreground"] = self.fg
            self.MessageLabel["background"] = self.bg

def main():
    """Instantiate and pop up the window."""
    GuessingGame().mainloop()


if __name__ == "__main__":
    main()
