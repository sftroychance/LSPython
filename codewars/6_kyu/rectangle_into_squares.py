# Cut a given "true" rectangle into squares ("true" rectangle meaning that the two dimensions are different).

# result = []
# given two values (5, 3) -> rectangle 5 x 3
# loop
# if values are equal, append value to result and return
# else append smallest value and subtract smallest from largest
# end loop

def sq_in_rect(length, width):
    if length == width:
        return None

    result = []

    while True:
        if length == width:
            result.append(length)
            return result
        elif length > width:
            result.append(width)
            length -= width
        else:
            result.append(length)
            width -= length

print (sq_in_rect(5, 3) == [3, 2, 1, 1])
print (sq_in_rect(6, 3) == [3, 3])
