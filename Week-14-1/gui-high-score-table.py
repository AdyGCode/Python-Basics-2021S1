# --------------------------------------------------------------
# File:     Week-14-1/gui-high-score-table-v3.py
# Project:  Python-Class-Demos
# Author:   Adrian Gould <Adrian.Gould@nmtafe.wa.edu.au>
# Created:  18/05/2021
# Purpose:  Create a High Score Table V2
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
                                           column=0,
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
                      row=1,
                      column=0,
                      columnspan=3,
                      sticky="EW",
                      foreground="#03a003")
        for counter in range(0, 5):
            bg_colour = "#ffffff"
            score = self.scores[counter]
            if counter % 2 == 0:
                bg_colour = "#cccccc"
            temp_panel = self.addPanel(row=6 + counter,
                                       column=0,
                                       background=bg_colour
                                       )
            temp_panel.addLabel(font="Trebuchet",
                                text=f"  {score['name']:<5}",
                                row=counter,
                                column=0,
                                sticky="W",
                                foreground="#333333",
                                background=bg_colour)
            temp_panel.addLabel(font="Trebuchet",
                                text=f"{score['score']:>5}  ",
                                row=counter,
                                column=1,
                                sticky="E",
                                foreground="#090909",
                                background=bg_colour)
            high_score_labels.append(temp_panel)


def main():
    """Instantiate and pop up the window."""
    HighScoreTable().mainloop()


if __name__ == "__main__":
    main()
