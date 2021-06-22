# File:     Week-4-1/loops-2.py
# Author:   Adrian Gould
# Purpose:  Demonstrate loops in Python

for count in range(1, 7):
    print(f"Count is {count}")

for count in range(6, 0, -1):
    print(f"Count is {count}")

for count in range(1, 7, 2):
    print(f"Count is {count}")

increment_by = 3
count = 1
while count < 20:
    print(f"Count is {count}, Increment is {increment_by}")
    count += increment_by  # count = count + increment_by
    if count % 2 == 0:
        increment_by = 3
    else:
        increment_by = 2

# for count in range(1, 20, increment_by):
#     print(f"Count is {count}, Increment is {increment_by}")
#     if count % 2 == 0:
#         increment_by = 3
#     else:
#         increment_by = 2

