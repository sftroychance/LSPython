# You are given an array(list) strarr of strings and an integer k. Your task is to return the first longest string consisting of k consecutive strings taken in the array.

# n being the length of the string array, if n = 0 or k > n or k <= 0 return ""

def longest_consec(strarr, k):
    if not strarr or k > len(strarr) or k <= 0:
        return ''

    concatenated = [''.join(strarr[i:i + k]) for i in range(len(strarr) - k + 1)]

    # for i in range(len(strarr) - k + 1):
        # concatenated.append(''.join(strarr[i:i + k]))

    return max(concatenated, key=len)

print(longest_consec(["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"], 2) == 'folingtrashy')
