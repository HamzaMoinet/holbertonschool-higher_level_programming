#!/usr/bin/env python3
"""Class SwimMin FlyMixin"""


class SwimMixin:
    """Swim"""
    def swim(self):
        print("The creature swims!")

class FlyMixin:
    """Fly"""
    def fly(self):
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    """Dragon"""
    def roar(self):
        print("The dragon roars!")
