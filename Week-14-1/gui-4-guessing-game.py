# ---------------------------------------------------------------------
# File:     Week-13-2/gui-4-guessing-game.py
# Project:  Python-Class-Demos
# Author:   Adrian Gould <Adrian.Gould@nmtafe.wa.edu.au>
# Created:  13/05/2021
# Purpose:  GUI Guessing Game version 4
#
# Duplicate the third version of the guessing game.
#
# You will enhance this version of the game by:
#   8) When the user wins, ask them for their initials (must be three
#   of the following characters: A-Z or asterisk (*).
#
#   9) Append the user initials and score to a file called
#   "HighScores.csv". They should be added in the form: "INITIALS",0
#
#   10) Add a Quit button that allows the user to exit the game - use
#   the self.quit() method to exit the application cleanly.
#
#   11) Add a label with the current number of guesses in the form:
#   "0 Guesses", "1 Guess", "2 Guesses"... etc.
#
#   12) Add a play again button, which will reset the guess count,
#   reset the guess input box, clear any messages, create a new
#   random number to be guessed.
# ----------------------------------------------------------------------
import string
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
        self.computer_number = randint(1, 10)
        self.message = ""
        self.fg = "#000000"
        self.bg = "#000000"
        self.game_won = False
        self.initials = ""

        # EasyFrame.__init__(self,
        #                    title="Guessing Game",
        #                    width=300,
        #                    height=150)
        super().__init__(title="Guessing Game",
                         width=300,
                         height=200)

        # Create the interface
        self.Title = \
            self.addLabel(text="Guess the Number",
                          row=0,
                          column=0,
                          columnspan=3,
                          sticky="EW",
                          font="Verdana",
                          foreground="#ffffff",
                          background="#000000")

        self.GuessLabel = \
            self.addLabel(text="What is your Guess?",
                          row=1,
                          column=0,
                          foreground="#090909")

        self.NumberGuessed = \
            self.addIntegerField(value=0,
                                 row=1,
                                 column=1)

        self.GuessButton = \
            self.addButton(text="Guess!",
                           row=1,
                           column=2,
                           command=self.check_guess)

        self.MessageLabel = \
            self.addLabel(text="take a guess..",
                          row=2,
                          column=0,
                          columnspan=3,
                          sticky="EW")

        self.CountLabel = \
            self.addLabel(text="0 Guesses",
                          row=3,
                          column=0,
                          sticky="EW")

        self.PlayAgainButton = \
            self.addButton(text="Play Again",
                           row=3,
                           column=1,
                           command=self.play_again,
                           state="disabled")

        self.QuitButton = \
            self.addButton(text="Quit",
                           row=3,
                           column=2,
                           command=self.quit_game,
                           state="normal")

        self.InitialsLabel = \
            self.addLabel(text="Enter Initials:",
                          row=4,
                          column=0,
                          foreground="#090909")

        self.SaveWinnerButton = \
            self.addButton(text="Save",
                           row=4,
                           column=2,
                           state="disabled",
                           command=self.filter_initials())

        self.InitialsText = \
            self.addTextField(row=4,
                              column=1,
                              state="normal")
        #
        # self.InitialsText.bind("<Return>",
        #                        lambda event: self.filter_initials())

    def check_guess(self):
        try:
            user_number = self.NumberGuessed.getNumber()
            self.count += 1
            if user_number > self.computer_number:
                self.show_message("Too High!",
                                  bg="#ff0000",
                                  fg="#ffffff")
            elif user_number < self.computer_number:
                self.show_message("Too Low!",
                                  bg="#0000ff",
                                  fg="#ffffff")
            else:
                self.show_message(
                    f"You got it in {self.count} guesses!",
                    bg="#00ff00",
                    fg="#000000")
                self.game_won = True
        except ValueError:
            self.show_message("You need to enter an integer",
                              bg="#ffbb00",
                              fg="#000000")
        finally:
            self.update_guesses(self.count)
            if self.game_won:
                self.winners_initials()
                self.save_score(self.initials, self.count)
                self.PlayAgainButton['state'] = "normal"

    def show_message(self, message="", fg="#000000", bg="#ffffff"):
        self.MessageLabel["text"] = message
        self.MessageLabel["foreground"] = fg
        self.MessageLabel["background"] = bg

    def update_guesses(self, current_count):
        guess_word = "Guesses"
        if current_count == 1:
            guess_word = "Guess"
        self.CountLabel["text"] = f"{current_count} {guess_word}"

    def play_again(self):
        # TODO: save game high score
        self.computer_number = randint(1, 100)
        self.count = 0
        self.game_won = False
        self.show_message("Try to guess my number, meat bag...",
                          fg="#000000",
                          bg="#ffffff")
        self.CountLabel["text"] = f"{self.count} Guesses"
        self.PlayAgainButton["state"] = "disabled"

    def quit_game(self):
        # TODO: save game high scores
        self.quit()

    def winners_initials(self, state="normal"):
        self.InitialsText['state'] = state
        self.SaveWinnerButton['state'] = state

    def filter_initials(self):
        initials_text = self.InitialsText['text'].getText()
        initials_text = initials_text.upper()
        allowed = string.ascii_uppercase + "*"
        self.initials = ""
        for letter in initials_text:
            if letter in allowed:
                self.initials += letter
        self.initials = self.initials[:3]
        self.winners_initials("disabled")

    def save_score(self, winner, score):
        with open("HighScores.csv", "a") as score_file:
            score_file.write(f'"{winner}", {score}\n')
        score_file.close()
        self.MessageLabel["text"] = "Saved"


def main():
    """Instantiate and pop up the window."""
    GuessingGame().mainloop()


if __name__ == "__main__":
    main()
