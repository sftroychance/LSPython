# Create a function taking a positive integer between 1 and 3999 (both included) as its parameter and returning a string containing the Roman Numeral representation of that integer.

def solution(n):
    ARABIC_TO_ROMAN = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }

    result = ''

    # while n > 0:
    #     for key, val in ARABIC_TO_ROMAN.items():
    #         if key <= n:
    #             result += val
    #             n -= key
    #             break

    # better: iterate over the hash just once

    for val, roman in ARABIC_TO_ROMAN.items():
        while n >= val:
            result += roman
            n -= val

    return result

print(solution(1000) == 'M')
print(solution(4) == 'IV')
print(solution(89) == 'LXXXIX')
