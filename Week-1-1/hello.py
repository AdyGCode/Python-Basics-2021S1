# Author:   Adrian Gould
# Purpose:  Quick outline (1 liner) of what code will do

# variables
name = "Adrian"
height = 1.79
names = ["Eileen Dover", "Jacques d'Carre", "Robyn Banks",
         "Jill Hill", "Humpty Dumpty"]
# Tidy Code (CARE) CTRL+ALT+L

for a_name in names:
    print(f"{a_name}")

    print(f"Hello {name}, welcome to Python")
    print(f"I detected that you are about {height:3.2}m tall")
