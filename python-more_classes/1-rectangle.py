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
        self._height = value
