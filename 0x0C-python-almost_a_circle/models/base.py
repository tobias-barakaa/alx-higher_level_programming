#!/usr/bin/python3
"""class Base function"""


class Base:
    """
    Base class for creating objects with an id attribute.

    Attributes:
        __nb_objects (int): Counter for generating unique ids.

    Methods:
        __init__(self, id=None): Initializes a Base object with a unique id.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a Base object with a unique id.

        Args:
            id (int): Optional id
        value. If provided, the object is assigned the given id.
                      If not provided, a
        unique id is generated for the object.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
