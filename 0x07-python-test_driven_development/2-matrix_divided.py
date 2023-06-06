#!/usr/bin/python3

def matrix_divided(matrix, div):
    """
    Perform division on each element of a matrix.

    Args:
        matrix (list of lists): The input matrix.
        div (int or float): The divisor.

    Raises:
        TypeError: If the matrix is not a matrix (list of lists) of integers/floats,
                   or if each row of the matrix does not have the same size,
                   or if the divisor is not a number.
        ZeroDivisionError: If the divisor is zero.

    Returns:
        list of lists: A new matrix with the division result.
    """

    # Validate the matrix and divisor
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Validate the size of each row in the matrix
    row_sizes = set(len(row) for row in matrix)
    if len(row_sizes) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    # Perform the division on each element
    new_matrix = []
    for row in matrix:
        new_row = []
        for elem in row:
            new_elem = elem / div
            rounded_result = round(new_elem, 1)
            new_row.append(rounded_result)
        new_matrix.append(new_row)

    return new_matrix
