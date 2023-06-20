#!/usr/bin/python3
"""
This module defines the Rectangle class that represents a rectangle.
"""

from models.base import Base


class Rectangle(Base):
    """
    Represents a rectangle, a subclass of the Base class.

    Attributes:
        width (int): Width of the rectangle.
        height (int): Height of the rectangle.
        x (int): x-coordinate of the rectangle's position.
        y (int): y-coordinate of the rectangle's position.
        id (int): Unique identifier for the rectangle.

    Methods:
        __init__(self, width, height, x=0, y=0, id=None):
        Initializes a Rectangle object.
        area(self): Calculates and returns the area of the rectangle.
        display(self): Prints a visual representation of the rectangle.
        update(self, *args, **kwargs): Updates
        the attributes of the rectangle.
        to_dictionary(self): Returns a dictionary representation
        of the rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle object with the given width,
        height, position, and id.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int): x-coordinate of the rectangle's position. Defaults to 0.
            y (int): y-coordinate of the rectangle's position. Defaults to 0.
            id (int): Optional id
            value. If provided, the
            rectangle is assigned the given id.
            If not provided, a unique id is generated for the rectangle.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        Getter for the width of the Rectangle.

        Returns:
            int: Width of the Rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width of the Rectangle.

        Args:
            value (int): New width value.

        Raises:
            TypeError: If the width is not an integer.
            ValueError: If the width is less than or equal to 0.
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter for the height of the Rectangle.

        Returns:
            int: Height of the Rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height of the Rectangle.

        Args:
            value (int): New height value.

        Raises:
            TypeError: If the height is not an integer.
            ValueError: If the height is less than or equal to 0.
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Getter for the x coordinate of the Rectangle.

        Returns:
            int: x coordinate of the Rectangle.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter for the x
        coordinate of the Rectangle.

        Args:
            value (int): New x coordinate value.

        Raises:
            TypeError: If the x coordinate is not an integer.
            ValueError: If the x coordinate is less
        """
