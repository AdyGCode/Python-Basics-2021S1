# --------------------------------------------------------------
# File:     Week-14-1/gui-high-score-table.py
# Project:  Python-Class-Demos
# Author:   Adrian Gould <Adrian.Gould@nmtafe.wa.edu.au>
# Created:  13/05/2021
# Purpose:  Create a High Score Table
#
# --------------------------------------------------------------
import csv

from breezypythongui import EasyFrame


class HighScoreTable(EasyFrame):
    def __init__(self):
        # [ {'name':'xxx', 'score':000}, ...]
        self.scores = []

        super().__init__(title="Guessing Game",
                         width=300,
                         height=200)

        self.ScoresButton = self.addButton(text="Show Scores",
                                           row=0,
                                           column=1,
                                           command=self.show_high_scores)

    def read_high_scores(self):
        lines = []
        with open("HighScores.csv", newline='') as csv_file:
            score_reader = csv.reader(csv_file)
            for row in score_reader:
                lines.append({'name': row[0], 'score': int(row[1])})
        return lines

    def show_high_scores(self):
        self.scores = self.read_high_scores()
        high_score_labels = []
        self.addLabel(font="Verdana",
                      text="BEST SCORES!",
                      row=4,
                      column=0,
                      columnspan=3,
                      sticky="EW",
                      foreground="#03a003")
        for counter in range(0, 5):
            user_score = self.scores[counter]
            temp_label = self.addLabel(font="Courier",
                                       text=f"{user_score['name']:<3}    "
                                            f"{user_score['score']:>3}",
                                       row=6 + counter,
                                       column=0,
                                       columnspan=3,
                                       sticky="EW",
                                       foreground="#090909")
            high_score_labels.append(temp_label)


def main():
    """Instantiate and pop up the window."""
    HighScoreTable().mainloop()


if __name__ == "__main__":
    main()
