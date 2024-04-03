# # Return the number (count) of vowels in the given string.

# # We will consider a, e, i, o, u as vowels for this Kata (but not y).

# The input string will only consist of lower case letters and/or spaces.

def get_count(sentence):
    # vowels = 'aeiou'
    # count = 0

    # for vowel in vowels:
    #     count += sentence.count(vowel)

    # return count

    return sum([1 for letter in sentence if letter in 'aeiou'])

print(get_count('aeiou'))
