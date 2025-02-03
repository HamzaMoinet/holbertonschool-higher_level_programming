#!/usr/bin/python3
class MyList(list):
    """A subclass"""
    def print_sorted(self):
        """print the list"""
        print(sorted(self))
