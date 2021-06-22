# File:     Week-6-1/encryption-1.py
# Author:   Adrian Gould
# Purpose:  Caesar Cypher

encrypted = ""
message = "fizz"
offset = -1

for character in message:
    ascii_code = ord(character)
    new_code = (ascii_code + offset - ord('a')) % 26 + ord('a')
    encrypted = encrypted + chr(new_code)

print(f"Encrypted message: {encrypted}")
