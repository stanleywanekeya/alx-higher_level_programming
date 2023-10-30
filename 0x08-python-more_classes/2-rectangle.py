#!/usr/bin/python
"""Defines class Rectangle"""


class Rectangle:
    """Represents class Rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes the Rectangle class

        Args:
            width (int): represents the width
            height (int): represents the height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """gets the width of the class"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """gets the height of class"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    def area(self):
        """calculates and returns rectangles area"""
        return width * height

    def perimeter(self):
        """calculates and returns rectangles perimente"""
        if self.__width == 0 and self.__height == 0:
            return 0
        return self.__width*2 + self.__height*2
