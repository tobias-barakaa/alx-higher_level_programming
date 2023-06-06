#!/usr/bin/python3

def text_indentation(text):
    """ 
    Function to print texts with indentation.

    Args:
        text (str): The text to print.

    Raises:
        TypeError: If the text is not a string.

    Returns:
        None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    for char in text:
        result += char
        if char in [".", ",", "?", ":"]:
            result += "\n\n"

    print(result)
