#!/usr/bin/python3
from models.base import Base
"""function"""


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
        __init__(self, width, height, x=0, y=0, id=None): Initializes a Rectangle object.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle object with the given width, height, position, and id.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int): x-coordinate of the rectangle's position. Defaults to 0.
            y (int): y-coordinate of the rectangle's position. Defaults to 0.
            id (int): Optional id value. If provided, the rectangle is assigned the given id.
                      If not provided, a unique id is generated for the rectangle.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter for the width of the rectangle.

        Returns:
            int: Width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width of the rectangle.

        Args:
            value (int): New width value.

        Raises:
            TypeError: If the width is not an integer.
            ValueError: If the width is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter for the height of the rectangle.

        Returns:
            int: Height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height of the rectangle.

        Args:
            value (int): New height value.

        Raises:
            TypeError: If the height is not an integer.
            ValueError: If the height is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Getter for the x-coordinate of the rectangle's position.

        Returns:
            int: x-coordinate of the rectangle's position.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter for the x-coordinate of the rectangle's position.

        Args:
            value (int): New x-coordinate value.

        Raises:
            TypeError: If the x-coordinate is not an integer.
            ValueError: If the x-coordinate is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Getter for the y-coordinate of the
