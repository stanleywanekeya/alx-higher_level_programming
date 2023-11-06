#!/usr/bin/python3
"""Creation of a base class"""


class BaseGeometry(obj):
    """Creation of baseclass BaseGeometry"""

    def area(self):
        """an empty function that raises an exception"""

        raise Exception("area() is not implemented")
