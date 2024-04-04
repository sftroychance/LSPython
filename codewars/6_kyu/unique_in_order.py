# Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

def unique_in_order(sequence):
    # from itertools import groupby

    # return [k for k, _ in groupby(sequence)]

    # groupby works, but another solution without import:

    return [x for idx, x in enumerate(sequence) if idx == 0 or x != sequence[idx - 1]]

print(unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B'])
