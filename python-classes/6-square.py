#!/usr/bin/python3
"""class Square that defines a square by: (based on 2-square.py)"""


class Square:
    """private attribute size"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square"""
        self._size = size
        self._position = position

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

    @property
    def position(self):
        """Getter for position"""
        return self._position

    @position.setter
    def position(self, value):
        """Setting for position"""
        if (type(value) is not tuple or len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self._position = value

    def area(self):
        """Calculate the area of the square"""
        return self._size ** 2

    def my_print(self):
        """Print a square with the character"""
        if self._size == 0:
            print("")
        else:
            print("\n" * self._position[1], end="")
            for i in range(self._size):
                print("_" * self._position[0] + "#" * self._size)
