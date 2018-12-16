#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    drom = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    no = 0
    for i in range(0, len(roman_string)):
        k = roman_string[i]
        if k in drom:
            if i < len(roman_string) - 1:
                l = roman_string[i + 1]
                if drom[k] < drom[l]:
                    no -= drom[k]
                else:
                    no += drom[k]
            else:
                no += drom[k]
    return no
