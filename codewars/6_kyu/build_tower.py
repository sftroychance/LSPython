# Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors. A tower block is represented with "*" character.

# pad is (n_floors * 2) -  1
# number of * is (floor * 2) - 1

def tower_builder(n_floors):
    line_size = n_floors * 2 - 1

    return [('*' * (floor * 2 - 1)).center(line_size)
            for floor in range(1, n_floors + 1)]

print(tower_builder(1))
print(tower_builder(3))
print(tower_builder(6))

