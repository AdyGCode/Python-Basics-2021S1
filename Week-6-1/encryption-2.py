"""
File:     Week-6-1/encryption-2.py
Author:   Adrian Gould
Purpose:  Caesar Cypher
          All printable characters from 32 to 127

Design:   Define constants (first and last character values)
          Define the number of characters between first and last
          printable characters (ascii_difference)
          Define the encrypted string (encrypted is "")
          Define the unencrypted string (message)
          Define the offset for the cypher (offset is 1)

          For each character in the message
              get the character's ascii code
              calculate the cyphered character code
              add the new character to the encrypted message

          Display the encrypted message
"""

FIRST_ASCII = 32  # ord(' ')
LAST_ASCII = 127  # ord(BackSpace)
ascii_difference = LAST_ASCII - FIRST_ASCII

encrypted = ""
message = "What did the Aussie Dalek Spy say when sending a message? " \
          "ENCRYPT MATE, ENCRYPT MATE!"
offset = 1


for character in message:
    ascii_code = ord(character)
    new_code = (ascii_code + offset - FIRST_ASCII) % ascii_difference \
               + FIRST_ASCII
    encrypted = encrypted + chr(new_code)

print(f"Encrypted message: {encrypted}")
