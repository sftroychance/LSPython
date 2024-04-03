# Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

# Examples:
# Input: 42145 Output: 54421

# Input: 145263 Output: 654321

# Input: 123456789 Output: 987654321

# A:
# convert to str
# split
# map to int
# sort desc key = int reverse=True
# map to str
# join
# convert to int

def descending_order(num):
    # chars = list(str(num))
    # chars.sort(key=int, reverse=True)
    # return int(''.join(chars))

    # using sorted (sort would not chain):
    return int(''.join(sorted(str(num), reverse=True)))

print(descending_order(12543))
