#!/usr/bin/python3
"""class BaseGeometry (based on 6-base_geometry.py)"""


class BaseGeometry:
    """cclass BaseGeometry (based on 6-base_geometry.py)"""
    def area(self):
        """exceptions raise"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """int authenticate"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
