#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for y in (matrix):
        new_matrix.append([x*x for x in y])
    return new_matrix
