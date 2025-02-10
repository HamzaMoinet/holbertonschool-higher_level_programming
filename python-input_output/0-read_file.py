#!/usr/bin/python3
"""fonction read file"""


def read_file(filename=""):
    """Read file"""
    with open(filename, 'r', encoding="utf-8") as f:
        content = f.read()
    print(content, end="")
