#!/usr/bin/env python3
"""CountedIterator class"""


class CountedIterator:
    """Iteraror with a counter."""
    def __init__(self, iterator):
        self.iterator = iter(iterator)
        self.count = 0

    def get_count(self):
        return self.count

    def __next__(self):
        """next"""
        item = next(self.iterator)
        self.count += 1
        return item
