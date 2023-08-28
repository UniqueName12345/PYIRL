"""
PYIRL - Python Input and Read Library
"""

__version__ = "0.0.1"
__author__ = "DifferentDance8"
__license__ = "MIT"
__copyright__ = "Copyright 2023 DifferentDance8"


def boolean_input(message, default=False):
    """
    Prompts the user for a boolean input and returns the corresponding boolean value.

    Parameters:
        message (str): The message to display to the user when prompting for input.
        default (bool, optional): The default value to return if the user does not provide any input. Defaults to False.

    Returns:
        bool: True if the user inputs 'y', False if the user inputs 'n', and the default value if the user does not provide any input and a default value is specified.
    """
    while True:
        value = input(message)
        if value.lower() == "y":
            return True
        elif value.lower() == "n":
            return False
        elif not value and default:
            return default


def input_with_default(message, default=""):
    """
    Prompts the user for input and returns the input value or the default value if the user does not provide any input.

    Parameters:
        message (str): The message to display to the user when prompting for input.
        default (str, optional): The default value to return if the user does not provide any input. Defaults to "".

    Returns:
        str: The input value or the default value if the user does not provide any input.
    """
    while True:
        value = input(message)
        if value:
            return value
        elif default:
            return default
