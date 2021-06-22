# File:     Week-6-1/decryption-2.py
# Author:   Adrian Gould
# Purpose:  Caesar Cypher Decryption
#           All printable characters from 32 to 127

encrypted = ""
message = "Qfsui-!fodszqujpo!ibt!mboefe\""
offset = 1
first_ascii = ord(' ')
last_ascii = 127  # ord(DEL)
ascii_difference = last_ascii - first_ascii

for character in message:
    ascii_code = ord(character)
    new_code = (ascii_code - offset - first_ascii) % ascii_difference \
               + first_ascii
    encrypted = encrypted + chr(new_code)

print(f"Encrypted message: {encrypted}")
