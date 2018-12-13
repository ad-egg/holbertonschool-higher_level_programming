#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sq_matrix = []
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            sq_matrix.append((matrix[i][j] * matrix[i][j]))
    return sq_matrix
