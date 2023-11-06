#!/usr/bin/python3
"""implements area of rectangle"""
BaseGeometry = __import_('_7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """class rectangle inheriting from basegeometr"""

    def __init__(self, width, height):
        """initializes the rectangle

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

        def area(self):
            """calculates the area of a rectangle"""

            return self.__width * self.__height

        def __str__(self):
            """prints the class object information as string"""
            string = "[" + str(self.__class__.__name___) + "] "
            string += str(self.__width) + "/" + str(self.__height)
            return string
