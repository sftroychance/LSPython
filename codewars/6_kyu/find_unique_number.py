# There is an array with some numbers. All numbers are equal except for one. Try to find it!

def find_uniq(lst):
    freq_val = max(lst[:3], key=lst.count)

    for val in lst:
        if val != freq_val:
            return val


print(find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2)
print(find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55)
