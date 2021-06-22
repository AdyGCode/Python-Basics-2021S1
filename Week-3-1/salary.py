# File:     Week-3-1/salary.py
# Author:   Adrian Gould
# Purpose:  Demonstrate calculations and formatting real numbers

hours_worked = 37.5  # number of hours per week
pay_rate = 22.75  # $ per hour
salary = hours_worked * pay_rate
print("Salary calculation")
print(f"Hours Worked:  {hours_worked:>6.2f}")
print(f"Pay Rate:     ${pay_rate:>6.2f}")
print(f"Salary:       ${salary:>6.2f}")
