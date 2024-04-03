# You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.

def get_middle(s):
    center_index = len(s) // 2

    if len(s) % 2 == 0:
        return s[center_index - 1:center_index + 1]
    else:
        return s[center_index]

print(get_middle('apple'))
print(get_middle('apples'))
