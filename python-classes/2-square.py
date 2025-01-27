#!/usr/bin/python3
"""class Square that defines a square"""


class Square:
    """private attribute size"""

    def __init__(self, size=0):
        """
        Args:
            size (self, size=0): Defaults to 0.

        Raises:
            TypeError: size must be an integer
            ValueError: ize must be >= 0
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
