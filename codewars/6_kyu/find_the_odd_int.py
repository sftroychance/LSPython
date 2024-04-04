# Given an array of integers, find the one that appears an odd number of times.

# There will always be only one integer that appears an odd number of times.

def find_it(seq):
    return [val for val in seq if seq.count(val) % 2 == 1][0]

print(find_it([1, 1, 2]) == 2)
print(find_it([1]) == 1)
