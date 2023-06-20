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
    @staticmethod
    def to_json_string(list_dictionaries):
    """
    Return the JSON string representation of a list of dictionaries.

    Args:
        list_dictionaries (list): List of dictionaries.

    Returns:
        str: JSON string representation of list_dictionaries.
    """
    if list_dictionaries is None or len(list_dictionaries) == 0:
        return "[]"
    return json.dumps(list_dictionaries)


    @classmethod
    def save_to_file(cls, list_objs):
    """
    Write the JSON string representation of list_objs to a file.

    Args:
        cls (class): Class.
        list_objs (list): List of instances that inherit from Base.
    """
        filename = "{:s}.json".format(cls.__name__)
        content = []

        if list_objs is not None:
            for obj in list_objs:
                content.append(cls.to_dictionary(obj))

        with open(filename, mode="w", encoding="utf-8") as file:
            file.write(cls.to_json_string(content))


    @staticmethod
    def from_json_string(json_string):
    """
    Return a list of dictionaries from the JSON string representation.

    Args:
        json_string (str): String representing a list of dictionaries.

    Returns:
        list: List of dictionaries.
    """
        if json_string is None or json_string == "":
            return []
         return json.loads(json_string)           
