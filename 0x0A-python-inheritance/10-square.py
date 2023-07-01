#!/usr/bin/python3
"""class to square"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class for square"""
    def __init__(self, size):
        """square instance"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """square"""
        return (self.__size * self.__size)
