#!/usr/bin/python3
def roman_to_int(roman_string):
    """function to convert roman number into int"""

    if not roman_string or type(roman_string) != str:
        return 0

    else:
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        i = 0

        while i <= len(roman_string) - 2:
            if roman_string[i] not in d.keys():
                return 0

            if i <= len(roman_string) - 2:
                frist = roman_string[i]
                second = roman_string[i + 1]

                if d[frist] < d[second]:
                    result -= d[frist]
                else:
                    result += d[frist]
            i += 1

        result += d[roman_string[i]]
        return result
