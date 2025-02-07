#!/usr/bin/env python3
"""Class Fish, Bird and FlyingFish"""


class Fish:
    """class fish
    """
    def swim(self):
        """Swim"""
        print("The fish is swimming")

    def habitat(self):
        """Habitat"""
        print("The fish lives in water")

class Bird:
    """Class Bird"""
    def fly(self):
        """Fly"""
        print("The bird is flying")

    def habitat(self):
        """Habitat"""
        print("The bird lives in the sky")

class FlyingFish(Fish, Bird):
    """Class FlyingFish"""
    def fly(self):
        """Fly"""
        print("The flying fish is comming!")

    def swim(self):
        """Swim"""
        print("The flying fish is swimming!")

    def habitat(self):
        """Habitat"""
        print("The flying fish lives both in water and the sky!")
