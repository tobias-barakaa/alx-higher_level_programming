#!/usr/bin/python3

"""0-rectangle, built for Holberton project 0x08 task 0.
"""


class Rectangle:
    """Empty class per task instructions, will be built upon in later tasks.
    """

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle object with width and height set to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method to retrieve the width of the rectangle.
        Returns:
            The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method to set the width of the rectangle.
        Args:
            value (int): The width value to be set.
        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getter method to retrieve the height of the rectangle.
        Returns:
            The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method to set the height of the rectangle.
        Args:
            value (int): The height value to be set.
        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
