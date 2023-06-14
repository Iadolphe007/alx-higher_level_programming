#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = []

    for row in matrix:
        squared_matrix = list(map(lambda x: x ** 2 if isinstance(x, int) else x, row))
        result.append(squared_matrix)

    return result
