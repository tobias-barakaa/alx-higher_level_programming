#!/usr/bin/python3

"""function that inherits from int"""


class MyInt(int):
    """
    Overrides the == operator to invert its behavior.
    """
    def __eq__(self, element):
        return not super().__eq__(element)

    """
    Overrides the != operator to invert its behavior.
    """
    def __ne__(self, element):
        return not super().__ne__(element)
