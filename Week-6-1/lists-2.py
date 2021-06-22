# File:     Week-6-1/lists-2.py
# Author:   Adrian Gould
# Purpose:  Working with lists


number_of_days = 0
rain = None
rainfall = []
while rain is None or rain >= 0.0:
    prompt = f"Enter the rainfall for day {number_of_days + 1}:"
    try:
        rain = float(input(prompt))
        if rain >= 0:
            rainfall.append(rain)
            number_of_days += 1
    except ValueError:
        break

total_rain = 0
day = 1
print(f"{'Day':>8} | {'Rainfall':>10}")
print(f"{'-' * 8:>8} | {'-' * 10:>10}")
for day_rain in rainfall:
    total_rain += day_rain
    print(f"{day:>8} | {day_rain:>10.2f}")
    day += 1

print(f"{'-'*8:>8} | {'-' * 10:>10}")

average_rain = total_rain / number_of_days

print(f"{'Total':>8}:  {total_rain:>10.2f}")
print(f"{'Average':>8}:  {average_rain:>10.2f}")
