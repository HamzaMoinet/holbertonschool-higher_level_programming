#!/usr/bin/env python3
"""Module to create class"""



from abc import ABC, abstractmethod
import math


class Shape(ABC):

    """Abstract class method"""
    @abstractmethod
    def area(self):
        """Area shape"""
        pass

    @abstractmethod
    def perimeter(self):
        """Perimeter shape"""
        pass


class Circle(Shape):
    """Class Circle from Shape"""

    def __init__(self, radius):
        """Instantiation the radius of Circle """

        self.radius = radius

    def area(self):

        """Area calcul of Circle"""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Perimeter calcul of Circle"""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Class Rectangle from Shape"""


    def __init__(self, width, height):
        """Instantiation the width and height of Rectangle """
        self.width = width
        self.height = height

    def area(self):
        """Area clacul of Rectangle"""
        return  self.height * self.width

    def perimeter(self):
        """perimeter calul of Rectangle"""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print the area and perimeter for Circle and Rectangle"""
    print(f"Area: {shape.area()}")
    print(f"Perimetre: {shape.perimeter()}")
