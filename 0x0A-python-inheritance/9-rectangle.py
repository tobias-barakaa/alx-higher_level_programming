#!/usr/bin/python3
"""defines rectangle class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle that inherits from
      BaseGeometry (7-base_geometry.py).
(task based on 8-rectangle.py)"""
    def __init__(self, width, height):
        """rectangle element initialise """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def __str__(self):
        """rectangle rep"""
        str_rep = "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
        return str_rep

    def area(self):
        """area returns"""
        return (self.__width * self.__height)
