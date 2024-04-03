# Usually when you buy something, you're asked whether your credit card number, phone number or answer to your most secret question is still correct. However, since someone could look over your shoulder, you don't want that shown on your screen. Instead, we mask it.

# Your task is to write a function maskify, which changes all but the last four characters into '#'.

def maskify(cc):
    # return (len(cc) - 4) * '#' + cc[-4:]
    return cc[-4:].rjust(len(cc), '#')

print(maskify('12345678') == '####5678')
print(maskify('123') == '123')
