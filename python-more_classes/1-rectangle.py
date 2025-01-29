#!/usr/bin/python3
"""class Rectangle that defines a rectangle."""

class Rectangle:
    """Private attribute width and height"""

    def __init__(self, width=0, height=0):
        """"Initialise the rectangle"""
        self._width = width
        self._height = height

    @property
    def width(self):
        """Getter for width"""
        return self._width

    @width.setter
    def width(self, value):
        """Setter for width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self._width = value

    @property
    def height(self):
        """Getter for height"""
        return self._height

    @height.setter
    def height(self, value):
        """Setter for height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self._height = value

    def area(self):
        """Calculate and return the area of the rectangle"""
        return self._width * self._height

    def perimeter(self):
        """Calcule and return the perimeter of the rectangle"""
        if self._width == 0 or self._height == 0:
            return 0
        return 2 * (self._width + self._height)
