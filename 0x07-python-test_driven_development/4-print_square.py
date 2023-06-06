#!/usr/bin/python3

def print_square(size):
    """
    Prints a square with the character '#'.

    Args:
        size (int): The size length of the square.

    Raises:
        TypeError: If the size is not an integer or a float.
        ValueError: If the size is less than 0.
        TypeError: If the size is a float and less than 0.

    Returns:
        None
    """
    if not isinstance(size, (int, float)):
        raise TypeError("size must be an integer")

    if isinstance(size, float):
        if size < 0:
            raise TypeError("size must be an integer")
        else:
            size = int(size)

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
