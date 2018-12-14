#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sq_matrix = []
    for i in range(0, len(matrix)):
        sq_matrix_row = []
        for j in range(0, len(matrix[i])):
            sq_matrix_row.append(matrix[i][j] * matrix[i][j])
        sq_matrix.append(sq_matrix_row)
    return sq_matrix
