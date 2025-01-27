#!/usr/bin/python3
"""class Square that defines a square by: (based on 2-square.py)"""


class Square:
    """private attribute size"""

    def __init__(self, size=0):
        """Initialize the square"""
        self._size = size

    @property
    def size(self):
        """Getter for size"""
        return self._size

    @size.setter
    def size(self, value):
        """Setting for size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self._size = value

    def area(self):
        """Calculate the area of the square"""
        return (self._size**2)

    def my_print(self):
        """Print a square with the character"""
        if self._size == 0:
            print("")
        else:
            for i in range(self._size):
                print(self._size * "#")
