# Write and test a program that computes the area of a circle.
# This program should request a number representing a radius
# as input from the user.
# It should use the formula 3.14 * radius ** 2
# to compute the area and then output this result suitably
# labeled.
import math
PI = math.pi

# INPUTS
radius = None
while radius is None or radius <= 0.0:
    try:
        radius = float(input("Enter the radius:"))
        if radius <= 0.0:
            print("ERROR: Radius must be greater than 0.0")
    except ValueError:
        print("ERROR: Radius must be a positive number")
        radius = None

# CALCULATIONS
area = PI * radius ** 2  # area = PI * radius * radius

# OUTPUTS
print(f"Area of a circle with radius {radius} is {area}")
