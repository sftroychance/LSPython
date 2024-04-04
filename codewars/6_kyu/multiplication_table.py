# Your task, is to create N×N multiplication table, of size provided in parameter.

def multiplication_table(size):
    # base_list = list(range(1, size + 1))
    # result = []

    # result += [
    #     [x * line for x in base_list]
    #     for line in range(1, size + 1)
    # ]

    # return result

    return [
        [x * line for x in list(range(1, size + 1))] for line in range(1, size + 1)
    ]

print(multiplication_table(3) == [[1,2,3],[2,4,6],[3,6,9]])
