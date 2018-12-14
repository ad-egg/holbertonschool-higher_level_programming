#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    no = 0
    for i in range(0, len(roman_string)):
        if roman_string[i] == 'I':
            if i < len(roman_string) - 1 and roman_string[i + 1] != 'I':
                no -= 1
            else:
                no += 1
        elif roman_string[i] == 'V':
            no += 5
        elif roman_string[i] == 'X':
            if i < len(roman_string) - 1 and roman_string[i + 1] == 'C':
                no -= 10
            else:
                no += 10
        elif roman_string[i] == 'L':
            no += 50
        elif roman_string[i] == 'C':
            if i < len(roman_string) - 1 and roman_string[i + 1] == 'M':
                no -= 100
            else:
                no += 100
        elif roman_string[i] == 'D':
            no += 500
        elif roman_string[i] == 'M':
            no += 1000
    return no
