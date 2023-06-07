#!/usr/bin/python3

import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrices using NumPy.

    Args:
        m_a (list): First matrix.
        m_b (list): Second matrix.

    Returns:
        The resulting matrix of the multiplication.

    Raises:
        ValueError: If the matrices are not valid for multiplication.

    """
    try:
        return np.matmul(m_a, m_b)
    except ValueError as error:
        raise ValueError("Matrices cannot be multiplied") from error

