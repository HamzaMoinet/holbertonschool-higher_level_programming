#!/usr/bin/python3
"""class Rectangle that defines a rectangle."""


class Rectangle:
    """Private attribute width and height"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """"Initialise the rectangle"""
        self._width = width
        self._height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """Calculate the area of the rectangle"""
        return self._height * self._width

    def perimeter(self):
        """Calcule the perimeter of the rectangle"""
        if self._width == 0 or self._height == 0:
            return 0
        return 2 * (self._height + self._width)

    def __str__(self):
        """"Return a string representation of the rectangle using '#"""
        if self._height == 0 or self._width == 0:
            return ""
        return "\n".join([str(self.print_symbol) * self._width for _ in range(self._height)])

    def __repr__(self):
        """Return a string representation for debugging"""
        return ("Rectangle({}, {})".format(self._width, self._height))

    def __del__(self):
        """Prints a message that delate regect"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
