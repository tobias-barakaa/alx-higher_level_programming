#!/usr/bin/python3

"""function"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Calculates the area of the geometry.

        Raises:
            Exception: If the area() method is not implemented in the subclass.
        """
        raise Exception("area() is not implemented")
