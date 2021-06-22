# --------------------------------------------------------------
# File:     Week-13-2/gui-3-guessing-game.py
# Project:  Python-Class-Demos
# Author:   Adrian Gould <Adrian.Gould@nmtafe.wa.edu.au>
# Created:  13/05/2021
# Purpose:  GUI Guessing Game version 3
#
# Duplicate the second version of the guessing game.
#
# You will enhance this version of the game by:
#   5) Add a new label that shows the number of guesses taken
#   starting at 1, and increment every time a new guess is made.
#   6) When the user guessed the number, disable the guess button.
#   7) When the user guesses the number, display a "play again"
#   button that will restart the game with a new number and the count
#   reset. Remember to enable the guess button and hide the play
#   again button.
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
        self.message = ""
        self.fg = "#000000"
        self.bg = "#000000"
        self.game_won = False

        # EasyFrame.__init__(self,
        #                    title="Guessing Game",
        #                    width=300,
        #                    height=150)
        super().__init__(title="Guessing Game",
                         width=300,
                         height=250)

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

        self.CountLabel = self.addLabel(text="0 Guesses",
                                        row=3,
                                        column=0,
                                        sticky="EW")

        self.PlayAgainButton = self.addButton(text="Play Again",
                                              row=3,
                                              column=1,
                                              command=self.play_again)

        self.QuitButton = self.addButton(text="Quit",
                                         row=3,
                                         column=2,
                                         command=self.quit_game)

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
                self.fg = "#000000"
                self.game_won = True
                # self.quit()

        except ValueError:
            self.message = "You need to enter an integer"
            self.bg = "#ffbb00"
            self.fg = "#000000"

        finally:
            self.MessageLabel["text"] = self.message
            self.MessageLabel["foreground"] = self.fg
            self.MessageLabel["background"] = self.bg
            self.CountLabel["text"] = f"{self.count} Guesses"
            # if self.game_won:

    def play_again(self):
        # TODO: save game high score
        self.computer_number = randint(1, 100)
        self.count = 0
        self.message = ""
        self.game_won = False
        self.fg = "#000000"
        self.bg = "#ffffff"
        self.MessageLabel["text"] = self.message
        self.MessageLabel["foreground"] = self.fg
        self.MessageLabel["background"] = self.bg
        self.CountLabel["text"] = f"{self.count} Guesses"

    def quit_game(self):
        # TODO: save game high scores
        self.quit()

def main():
    """Instantiate and pop up the window."""
    GuessingGame().mainloop()


if __name__ == "__main__":
    main()
