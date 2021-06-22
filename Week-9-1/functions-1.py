# --------------------------------------------------------------
# File:     Week-9-1/functions-1.py
# Project:  Python-Class-Demos
# Author:   Adrian Gould <Adrian.Gould@nmtafe.wa.edu.au>
# Created:  13/04/2021
# Purpose:  Demonstrate functions using temperature conversions
#
# Define Problem:
#   Ask the user for a temperature in Celsius
#   Convert temperature to Fahrenheit
#   Convert temperature to Kelvin
#   Display temperatures in a table
#
# Test Data:
#   0C          32F       273.15K
#   28C         82.4F     301.15K
#   27.778C     82F       300.928K
#  -100C      -148F       173.15K
#   100C       212F       373.15K
#  -273.15C   -459.67F      0K
# --------------------------------------------------------------


def get_float(prompt="Enter a decimal number: ",
              minimum=-999999999.999,
              maximum=999999999.999):
    """
    Obtain user input as a floating point (decimal) number

    :param prompt: string - The prompt you want to display to the user
    :param minimum: float - the minimum value allowed
    :param maximum: float - the maximum value allowed
    :return: float - the user's entered decimal number
    """
    number = None
    while number is None:
        try:
            number = float(input(prompt))
            if number < minimum:
                number = None
                print(f"Value must be greater than {minimum:.2f}")
            elif number > maximum:
                number = None
                print(f"Value must be smaller than {maximum:.2f}")
        except ValueError:
            number = None
            print("Sorry, not a valid decimal value.")
    return number


def get_temperature_in_celsius():
    """
    Ask user for the temperature

    :return: float - temperature in Celsius
    """
    celsius = get_float(prompt="Enter temperature in Celsius: ",
                        minimum=-273.15)
    return celsius


def celsius_2_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit

    C = (F - 32) * 5 / 9
    F = (9 * C / 5) + 32

    :param celsius: float
    :return: float - the temperature in Fahrenheit
    """
    fahrenheit = (9 * celsius / 5.0) + 32
    return fahrenheit


def celcius_2_kelvin(celsius):
    """
    Convert Celsius to Kelvin

    0 Kelvin is -273.15 Celsius

    :param celsius: float
    :return: float - temperature in Kelvin
    """
    kelvin = celsius + 273.15
    return kelvin


def show_results(celsius, fahrenheit, kelvin):
    """
    Display table of results

    :param celsius: float
    :param fahrenheit: float
    :param kelvin: float
    """
    print(f"+{'-' * 38}+")
    print(f"|    Celsius | Fahrenheit |     Kelvin |")
    print(f"|{celsius:>11.2f} |{fahrenheit:>11.2f} |{kelvin:>11.2f} |")
    print(f"+{'-' * 38}+")


def main():
    temperature_c = get_temperature_in_celsius()
    temperature_f = celsius_2_fahrenheit(temperature_c)
    temperature_k = celcius_2_kelvin(temperature_c)
    show_results(temperature_c, temperature_f, temperature_k)


if __name__ == "__main__":
    main()
