#!/usr/bin/python3
"""Creates a subclass"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class rectangle inheriting from basegeometry"""

    def __init__(self, width, height):
        """initialises rectangle

        Args:
            width (int): width of rectangle
            height (int): height of rectanle
        """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
