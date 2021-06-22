"""
File:     Week-5-1/strings-1.py
Author:   Adrian Gould
Purpose:  Strings in Python
"""

given_name = "Adrian"
family_name = 'Gould'

# CTRL+ALT+L    Reformat code       CMD+ALT+L
# CTRL+D        Duplicate Line      CMD+D

print(given_name)
print(given_name, family_name)
print(len(given_name))  # length of the string
print(family_name[0])  # give FIRST character of string
print(family_name[-1])  # give LAST character from the string
print(given_name[0:2])  # give 1st TWO characters
print(given_name[:2])  # give 1st TWO characters
print(family_name[-4:])  # last four characters
print(family_name[:-4])  # all chars up to the 4th from end
print(family_name[1:-2])  # all chars from 2nd to 2nd last
print("@"[0:-1])  # gives nothing
print(family_name[::2])  # every 2nd character
print(family_name[::-2])  # every 2nd character in reverse

result = family_name[0:-20]
print(result)
print(type(result))  # Tells us the type of the result

print(family_name.upper())  # convert to upper case
print(family_name.lower())  # convert to lower case
print(family_name.swapcase())  # swap the upper to lower & visa versa

