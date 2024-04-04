# Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

# HH = hours, padded to 2 digits, range: 00 - 99
# MM = minutes, padded to 2 digits, range: 00 - 59
# SS = seconds, padded to 2 digits, range: 00 - 59
# The maximum time never exceeds 359999 (99:59:59)

# hours, remainder = divmod(seconds, 3600)
# minutes, seconds = divmod(remainder, 60)

def make_readable(seconds):
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    return f'{hours:02}:{minutes:02}:{seconds:02}'

print(make_readable(0) == '00:00:00')
print(make_readable(3599) == '00:59:59')
print(make_readable(86400) == '24:00:00')
