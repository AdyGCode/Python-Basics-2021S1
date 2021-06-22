# --------------------------------------------------------------
# File:     Week-13-2/gui-1-guessing-game.py
# Project:  Python-Class-Demos
# Author:   Adrian Gould <Adrian.Gould@nmtafe.wa.edu.au>
# Created:  13/05/2021
# Purpose:  GUI Guessing Game
#
# Write a guessing game that has the computer generate a secret
# random number between 1 and 100 (inclusive).
# The user will enter a number and the computer will respond
# with a message that tells the user if they need to guess
# higher or lower.
# The user keeps entering their guesses until they correctly enter
# the computer's secret number.
# The computer keeps track of how many guesses the user takes and
# when the number is correctly guessed, the computer will
# congratulate the user and show how many guesses they took.
# --------------------------------------------------------------
from random import random, randint

from breezypythongui import EasyFrame


class GuessingGame(EasyFrame):
    """Guessing Game Class

    Inherits the EasyFrame methods and properties
    """

    def __init__(self):
        """Initialise the frame and instance variables"""
        self.count = 0
        self.computer_number = randint(1, 100)
        self.message = ""

        super().__init__(title="Guessing Game",
                         width=300,
                         height=150)

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
                                          columnspan=3)

    # Command handling methods are added after this
    def check_guess(self):
        # create the method code here
        # delete pass when adding code
        try:
            user_number = self.NumberGuessed.getNumber()
            self.count += 1
            if user_number > self.computer_number:
                self.message = "Too High!"
            elif user_number < self.computer_number:
                self.message = "Too Low!"
            else:
                self.message = f"You got it in {self.count} guesses!"
                # self.quit()

        except ValueError:
            self.message = "You need to enter an integer"
        finally:
            self.MessageLabel["text"] = self.message


def main():
    """Instantiate and pop up the window."""
    GuessingGame().mainloop()


if __name__ == "__main__":
    main()
