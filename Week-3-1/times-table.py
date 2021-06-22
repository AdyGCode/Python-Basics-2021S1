# File:     Week-3-1/times-table.py
# Author:   Adrian Gould
# Purpose:  Display the 7 times table from 1 to 12
#  1 x 7 = 7
#  2 x 7 = 14
#  ...
# 10 x 7 = 70
# 11 x 7 = 77
# 13 x 7 = 84

multiplier = 7
print(f"{multiplier} times table...")
print(f"{'='*10:^30}")
for count in range(1, 13):
    result = count * multiplier
    print(f"{count:>2} x {multiplier:>2} = {result:>4}")
