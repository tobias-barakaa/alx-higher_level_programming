#!/usr/bin/python3

def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj: The object for which to retrieve the attributes and methods.

    Returns:
        A list containing the names of the attributes and methods available for the object.

    Examples:
        >>> lookup(MyClass1)
        ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
        '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__',
        '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__',
        '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
        '__subclasshook__', '__weakref__']

        >>> lookup(MyClass2)
        ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
        '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__',
        '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__',
        '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
        '__subclasshook__', '__weakref__', 'my_attr1', 'my_meth']

        >>> lookup(int)
        ['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__',
        '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__',
        '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__',
        '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__int__',
        '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__',
        '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__',
        '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__',
        '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__',
        '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__',
        '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__',
        '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate',
        'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
    """
    return dir(obj)
