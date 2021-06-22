# File:     Week-3-1/loops.py
# Author:   Adrian Gould
# Purpose:  Demonstrate loops in Python

# For loop - with maximum number
print("For Loop: Maximum number")
for counter in range(5):
    print(f"Count: {counter}")

# For loop - with maximum number
print("For Loop: Minimum and Maximum number")
for counter in range(1, 5):
    print(f"Count: {counter}")

# For loop - going backwards
print("For Loop: Minimum and Maximum number, backwards")
for counter in range(8, 2, -1):
    print(f"Count: {counter}")

# For loop - increase by 3
print("For Loop: increase by 3")
for counter in range(1, 10, 3):
    print(f"Count: {counter}")

for lines in range(5):
    print(f"Row: {lines}")
    for columns in range(6):
        print("*", end=" ")
    print()

# Draw a triangle
# *
# **
# ***
# ****

length_side = 4
for line in range(length_side):
    for stars in range(line + 1):
        print("*", end="")
    print()

triangle_height = 6
for line in range(triangle_height):
    print("*" * (line + 1))
