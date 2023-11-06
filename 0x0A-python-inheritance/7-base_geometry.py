#!/usr/bin/python3
"""creatrion of class"""


class BaseGeometry(obj):
    """creation of baseclass BaseGeometry"""

    def area(self):
        """Implements an empty area"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates arguments

        Args:
            name (string): string arguments
            value (int): integer arguments
        Raises:
            TypeError: checks for int
            Value: checks for absolute value
        """

        if not isinstance(int, value):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
