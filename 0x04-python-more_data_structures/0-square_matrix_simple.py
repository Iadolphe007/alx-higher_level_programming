#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = []

    for row in matrix:
        square = list(map(lambda x: x**2 if isinstance(x, int) else x, row))
        result.append(square)

    return result
