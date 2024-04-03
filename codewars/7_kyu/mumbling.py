# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"

# A:
# split
# initialize result list
# iterate with index
# result append letter.upper() + (index * letter.lower())
# return result joined with -

def accum(st):
    # result = []

    # for idx, char in enumerate(list(st)):
    #     result.append(char.upper() + (char.lower() * idx))
    # return '-'.join(result)
    return '-'.join([x.upper() + x.lower() * idx for idx, x in enumerate(st)])

print(accum("abcd") == "A-Bb-Ccc-Dddd")
print(accum("RqaEzty") == "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy")
