#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    rom = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }

    count = 0
    n = len(roman_string)

    for i in range(n):
        if i < n - 1 and rom[roman_string[i]] < rom[roman_string[i+1]]:
            count -= rom[roman_string[i]]
        else:
            count += rom[roman_string[i]]

    return count
