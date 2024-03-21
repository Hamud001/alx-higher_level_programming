#!/usr/bin/python3
#Hamud001


def roman_to_int(roman_string):
    """function converts a roman numeral to an integer."""
    if (not isinstance(roman_string, str) or
            roman_string is None):
        return (0)

    roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
    }
    value = 0

    for n in range(len(roman_string)):
        if roman_dict.get(roman_string[n], 0) == 0:
            return (0)

        if (n != (len(roman_string) - 1) and
                roman_dict[roman_string[n]] < roman_dict[roman_string[n + 1]]):
                value += roman_dict[roman_string[n]] * -1

        else:
            value += roman_dict[roman_string[n]]
    return (value)
