# Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

def solution(text, ending):
    return text.endswith(ending)

print(solution('abc', 'bc') == True)
print(solution('abc', 'd') == False)
