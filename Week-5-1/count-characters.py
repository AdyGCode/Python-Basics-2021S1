"""
File:     Week-5-1/count-characters.py
Author:   Adrian Gould
Description:
  To count the number of vowels, consonants and other characters in a
  string entered by the user

Tricks:
    "fred".find('e') --> 2 (found at position 2)
    "fred".find('x') --> -1 (not found)

Design:
  ask user for a string (some text)
  vowels is 'aeiou'
  consonants is 'bcdfghjklmnpqrstvwxyz'
  count of vowels is 0
  count of consonants is 0
  count of other is 0
  for each letter in user input
      if letter in vowels
          increment count of vowels
      else if letter in consonants
          increment count of consonants
      else
          increment count of other
      end if
  end for
  output results

Test Data:
  birdy
  Australia
  Llanfairpwllgwyngyllgogerychwyrndrobwllllantisiliogogogoch
"""

the_string = input("Enter some text:")
vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"
count_of_vowels = 0
count_of_consonants = 0
count_of_other = 0

for letter in the_string.lower():
    if vowels.find(letter) >= 0:
        count_of_vowels += 1
    elif consonants.find(letter) >= 0:
        count_of_consonants += 1
    else:
        count_of_other += 1
    # end if
# end for

print(f"Number of Vowels:     {count_of_vowels}")
print(f"Number of Consonants: {count_of_consonants}")
print(f"Number of Others:     {count_of_other}")
