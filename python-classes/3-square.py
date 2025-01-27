#!/usr/bin/python3
"""class Square that defines a square by: (based on 2-square.py)"""


class Square:
    """private attribute size"""

    def __init__(self, size=0):
        """_summary_

        Args:
            size (self, size=0): Defaults to 0.

        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self._size = size
    def area(self):
        """_summary_

        Returns:
            self._size**2: calcul area of square
        """
        return (self._size**2)
