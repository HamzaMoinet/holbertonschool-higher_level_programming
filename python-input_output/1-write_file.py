#!/usr/bin/python3
"""fonction write file"""


def write_file(filename="", text=""):
    """White file"""
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
