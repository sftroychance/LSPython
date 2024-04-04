# Write an algorithm that will identify valid IPv4 addresses in dot-decimal format. IPs should be considered valid if they consist of four octets, with values between 0 and 255, inclusive.


def is_valid_IP(strng):
    octets = [
        x for x in strng.split('.')
        if x.isdigit()
        if len(x) == len(str(int(x)))
        if 0 <= int(x) <= 255
    ]

    return len(octets) == 4 and strng.count('.') == 3


print(is_valid_IP('1.2.3.4') == True)
print(is_valid_IP('1.2.3') == False)
print(is_valid_IP('0.0.0.0') == True)
print(is_valid_IP('') == False)
