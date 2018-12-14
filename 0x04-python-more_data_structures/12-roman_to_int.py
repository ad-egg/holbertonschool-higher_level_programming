#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return 0
    no = 0
    for i in range(0, len(roman_string)):
        if roman_string[i] == 'D':
            no += 500
        elif roman_string[i] == 'C':
            no += 100
        elif roman_string[i] == 'L':
            no += 50
        elif roman_string[i] == 'I':
            if i < len(roman_string) - 1:
                if roman_string[i + 1] == 'X':
                    no += 9
                elif roman_string[i + 1] == 'V':
                    no += 4
                elif roman_string[i + 1] == 'I':
                    no += 1
            else:
                no += 1
            i += 1
        elif roman_string[i] == 'X':
                no += 10
        elif roman_string[i] == 'V':
                no += 5
    return no
