#!/usr/bin/python3
"""Prints full name"""


def say_my_name(first_name, last_name=""):
    """Function to print fullname

        Args:
            first_name (str): string
            second_name (str): string argument
        Raises:
            TypeError: if first name or last name are not strings

        """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
