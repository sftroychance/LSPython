# Let us consider this example (array written in general format):

# ls = [0, 1, 3, 6, 10]

# Its following parts:

# ls = [0, 1, 3, 6, 10]
# ls = [1, 3, 6, 10]
# ls = [3, 6, 10]
# ls = [6, 10]
# ls = [10]
# ls = []
# The corresponding sums are (put together in a list): [20, 20, 19, 16, 10, 0]

# The function parts_sums (or its variants in other languages) will take as parameter a list ls and return a list of the sums of its parts as defined above.

def parts_sums(ls):
    # return [sum(ls[i:]) for i in range(len(ls) + 1)]
    # too inefficient! (times out on codewars)

    # sums = [sum(ls)]

    # for i in range(1, len(ls) + 1):
    #     sums.append(sums[-1] - ls[i - 1])

    # return sums

    sums = [sum(ls)]

    # for i in range(len(ls)):
    #   sums.append(sums[-1] - ls[i])
    for item in ls:
        sums.append(sums[-1] - item)

    # below works, but it is not appropriate to use a list comprehension if you are not returning a list! you would be using the comprehension only for it side effects. Use a loop instead.
    # [sums.append(sums[-1] - ls[i]) for i in range(len(ls))]

    return sums


print(parts_sums([1, 2, 3, 4, 5, 6] ) == [21, 20, 18, 15, 11, 6, 0])
print(parts_sums([0, 1, 3, 6, 10]) == [20, 20, 19, 16, 10, 0])
