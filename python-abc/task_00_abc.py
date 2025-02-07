#!/usr/bin/env python3
"""Module to create class"""



from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract class animal"""

    @abstractmethod
    def sound(self):
        """Sound animal"""
        pass


class Dog(Animal):
    """Represent a dog"""

    def sound(self):
        """return sound of dog"""
        return "Bark"


class Cat(Animal):
    """Represent Cat"""

    def sound(self):
        """return sound of cat"""
        return "Meow"
