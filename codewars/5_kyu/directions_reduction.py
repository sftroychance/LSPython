# Write a function dirReduc which will take an array of strings and returns an array of strings with the needless directions removed (W<->E or S<->N side by side).

def dir_reduc(arr):
    import re

    dir_string = ' '.join(arr)

    ns, sn, ew, we = 'NORTH SOUTH', 'SOUTH NORTH', 'EAST WEST', 'WEST EAST'

    while True:
        if re.search(f'{ns}|{sn}|{ew}|{we}', dir_string):

            dir_string = re.sub(f'{ns}|{sn}|{ew}|{we}', '', dir_string)
            dir_string = re.sub('\s+', ' ', dir_string).strip()
        elif dir_string:
            return dir_string.split(' ')
        else:
            return []


print(dir_reduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]) == ['WEST'])
print(dir_reduc(["NORTH", "SOUTH", "EAST", "WEST", "NORTH", "NORTH", "SOUTH", "NORTH","WEST", "EAST"]) == ['NORTH', 'NORTH'])
print(dir_reduc(['NORTH', 'SOUTH']))
