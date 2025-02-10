#!/usr/bin/python3
"""fonction append_write"""


def append_write(filename="", text=""):
    """Append Write"""
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
