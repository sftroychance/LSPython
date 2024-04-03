# Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

def xo(s):
    lcase_s = s.lower()
    return lcase_s.count('x') == lcase_s.count('o')

print(xo('xxoo') == True)
print(xo('xoo') == False)
