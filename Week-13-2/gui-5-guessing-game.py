# --------------------------------------------------------------
# File:     Week-13-2/gui-5-guessing-game.py
# Project:  Python-Class-Demos
# Author:   Adrian Gould <Adrian.Gould@nmtafe.wa.edu.au>
# Created:  13/05/2021
# Purpose:  GUI Guessing Game version 5
#
# Duplicate the fourth version of the guessing game.
#
# You will enhance this version of the game by:
#
#   11) Add the provided code below to your GuessingGame class
# --------------------------------------------------------------


# Immediately after your "Guessing Game" class add:
# self.scores = []


# after the __init__ method for the "Guessing game" class, add:

#     def show_high_scores(self):
#         high_score_labels = []
#         self.addLabel(font="Verdana",
#                       text="BEST SCORES!",
#                       row=4,
#                       column=0,
#                       columnspan=3,
#                       sticky="EW",
#                       foreground="#090909")
#         for counter in range(0, 5):
#             user_score = self.scores[counter]
#             temp_label = self.addLabel(font="Courier",
#                                        text=f"{user_score['name']:<3}    "
#                                             f"{user_score['score']:>3}",
#                                        row=6 + counter,
#                                        column=0,
#                                        columnspan=3,
#                                        sticky="EW",
#                                        foreground="#090909")
#             high_score_labels.append(temp_label)



