#!/usr/bin/python3
"""function to pascal"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle of n rows
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize with the first row [1]

    for i in range(1, n):
        row = [1]  # First element of each row is always 1

        # Calculate the values for the current row
        for j in range(1, i):
            value = triangle[i-1][j-1] + triangle[i-1][j]
            row.append(value)

        row.append(1)  # Last element of each row is always 1

        triangle.append(row)  # Add the current row to the triangle

    return triangle
