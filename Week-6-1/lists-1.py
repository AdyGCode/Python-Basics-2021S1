# File:     Week-6-1/lists-1.py
# Author:   Adrian Gould
# Purpose:  Simple Lists


names = ["Jack", "Jill", "Jane", "John", "Jacqueline"]
details = ["Jacques d'Carre", 36, "123 Street, Sesame"]

# Using a single index gives the data from that position
print(names[1])  # Jill
print(names[-1])  # Jacqueline

# Using a slice gives a list
print(names[:2])  # ['Jack', 'Jill']
print(names[2:])  # ['Jane', 'John', 'Jacqueline']
print(names[2:-2])  # ["Jane"]
print(names[3:-2])  # []

