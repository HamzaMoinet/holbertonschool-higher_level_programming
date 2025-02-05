#!/usr/bin/python3
"""Improve Geometry"""


class BaseGeometry:
    """class BaseGeo"""

    def area(self):
        """Public instance"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """that validates value"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Class Rectangle from BaseGeometry"""

    def __init__(self, width, height):
        """Instantiation with width and height"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """area"""
        return self.__width * self.__height

    def __str__(self):
        """return, the following rectangle description"""
        return (f"[Rectangle] {self.__width}/{self.__height}")


class Square(Rectangle):
    """Class Square from Rectangle"""

    def __init__(self, size):
        """Instantiation with self"""
        self.integer_validator("self", size)
        self.__size = size
        super().__init__(size, size)

    def size(self):
        """Getter for size"""
        return self.__size

    def area(self):
        """Return area of the Square"""
        return self.__size * self.__size

    def __str__(self):
        """Return the string for Square"""
        return (f"[Square] {self.__size}/{self.__size}")
