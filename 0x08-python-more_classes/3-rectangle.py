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

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Returns:
            The perimeter of the rectangle.
            If width or height is equal to 0, returns 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Return a string representation of the rectangle.

        Returns:
            A string representing the rectangle using '#' characters.
            If width or height is equal to 0, returns an empty string.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return '\n'.join(['#' * self.__width] * self.__height)

    def __repr__(self):
        """
        Return a string representation of the rectangle.

        Returns:
            A string representation of the rectangle object.
        """
        return f"Rectangle(width={self.__width}, height={self.__height})"