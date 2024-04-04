# Write a function that takes an array of numbers (integers for the tests) and a target number. It should find two different items in the array that, when added together, give the target value. The indices of these items should then be returned in a tuple / list (depending on your language) like so: (index1, index2).

# For the purposes of this kata, some tests may have multiple answers; any valid solutions will be accepted.

# The input will always be valid (numbers will be an array of length 2 or greater, and all of the items will be numbers; target will always be the sum of two different items from that array).

# use two-pointer solution with sorted
# if sum > target move end pointer left
# if sum < target move start pointer right
# return index positions of the values in original list

def two_sum(numbers, target):
    sorted_list = sorted(numbers)
    start = 0
    end = len(numbers) - 1

    while start < end:
        current_sum = sorted_list[start] + sorted_list[end]

        if current_sum == target:
            break
        elif current_sum > target:
            end -= 1
        elif current_sum < target:
            start += 1

    first_idx = numbers.index(sorted_list[start])
    second_idx = numbers.index(sorted_list[end])

    if first_idx == second_idx:
        second_idx = (numbers.index(sorted_list[end])
                      or numbers.index(sorted_list[end], first_idx + 1))

    return (first_idx, second_idx)

    # First solution is long and complicated by the fact that the original list is not sorted

    # Another option:
    # set all values to dict keys
    # iterate over all values and see if difference key exists
    # problem: if value is repeated value is overwritten

    # Another option: brute force (O(n^2))

print(two_sum([1, 2, 3], 4))
# returns (0, 2) or (2, 0)
print(two_sum([3, 2, 4], 6))
# returns (1, 2) or (2, 1)
