# Implement a function that accepts 3 integer values a, b, c. The function should return true if a triangle can be built with the sides of given length and false in any other case.

# (In this case, all triangles must have surface greater than 0 to be accepted).

# Triangle inequality theorem: the sum of any two sides of a triangle is always greater than the third side

def is_triangle(a, b, c):
    return (a + b > c) and (b + c > a) and (a + c > b)


print(is_triangle(1, 2, 2) == True)
print(is_triangle(4, 2, 3) == True)
print(is_triangle(1, 2, 3) == False)
