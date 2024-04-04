# Write a simple parser that will parse and run Deadfish.

# Deadfish has 4 commands, each 1 character long:

# i increments the value (initially 0)
# d decrements the value
# s squares the value
# o outputs the value into the return array
# Invalid characters should be ignored.

def parse(data):
    val = 0
    result = []

    for char in data:
        match char:
            case 'i': val += 1
            case 'd': val -= 1
            case 's': val *= val
            case 'o': result.append(val)

    return result


print(parse('iiisdoso') == [8, 64])
