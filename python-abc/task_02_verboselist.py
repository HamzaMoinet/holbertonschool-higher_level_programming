#!/usr/bin/env python3
"""Extending the Python List with Notifications"""


class VerboseList(list):
    """class named VerboseList that extends the Python list class"""

    def append(self, item):
        """append"""
        super().append(item)
        print(f"Added {[item]} to the list.")

    def extend(self, iterable):
        """extend"""
        super().extend(iterable)
        print(f"Extended the list with [{len(iterable)}] items.")

    def remove(self, item):
        """remove"""
        print(f"Removed {[item]} from the list.")
        super().remove(item)

    def pop(self, index = -1):
        """Pops an item from the list and prints a notification."""
        item = self[index]
        print(f"Popped {[item]} from the list.")
        return super().pop(index)
