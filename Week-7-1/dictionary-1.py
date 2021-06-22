"""
File:       Week-7-1/dictionary-1.py
Author:     Adrian Gould
Purpose:    Demonstrate dictionaries
            Shows how to count the letters in a word
            Shows a simple bar chart of the counts
            Example for Abracadabra:
                {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}
                a: #####
                b: ##
                r: ##
                c: #
                d: #

Design:
    Define word (eg Abracadabra)
    Define letters as an empty dictionary
    Make word lower case
    For each letter in the word
        If the letter is in the dictionary
            Increment the dictionary count for the letter
        Else
            Add the letter to the dictionary with a count of 1

    Display the dictionary of letters/counts

    For each key in the letters dictionary:
        Display key, and a # letter count times

"""

word = "Abracadabra"
letters = {}
word = word.lower()
for key_letter in word:
    if letters.get(key_letter, False):
        letters[key_letter] += 1
    else:
        letters[key_letter] = 1

print(letters)

for key in letters:
    print(f"{key}: {'#' * letters[key]}")
