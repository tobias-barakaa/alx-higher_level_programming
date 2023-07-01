#!/usr/bin/python3
"""class inherit from rect"""


Rectangle = __import__('8-rectangle').Rectangle


class Square(Rectangle):
    """square inherit from rectangle"""
    def __init__(self, size):
        """initialise"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """returns sq"""
        return (self.__size * self.__size)

    def __str__(self):
        """square rep"""
        str_rep = "[Square] " + str(self.__size) + "/" + str(self.__size)
        return str_rep
