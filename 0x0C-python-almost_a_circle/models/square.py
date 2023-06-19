#!/usr/bin/python3
"""function to inherit"""
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square instance.

        Args:
            size (int): Size of the square.
            x (int): X-coordinate of the square's position.
            y (int): Y-coordinate of the square's position.
            id (int): Identifier of the square.

        Attributes:
            size (int): Size of the square.
            x (int): X-coordinate of the square's position.
            y (int): Y-coordinate of the square's position.
            id (int): Identifier of the square.
        """
        super().__init__(size, size, x, y, id)

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the Square.

        Args:
            *args: Variable-length arguments (no-keyworded arguments).
                1st argument should be the id attribute.
                2nd argument should be the size attribute.
                3rd argument should be the x attribute.
                4th argument should be the y attribute.
            **kwargs: Keyworded arguments represented as key/value pairs.

        Notes:
            If *args exists and is not empty, **kwargs is skipped.
            Each key in **kwargs represents an attribute to be updated.
        """
        if args:
            attrs = ["id", "size", "x", "y"]
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """
        Returns a string representation of the Square.

        Returns:
            str: String representation of the Square.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def to_dictionary(self):
        """
        Returns the dictionary representation of the Square.

        Returns:
            dict: Dictionary representation of the Square.
        """
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
