#!/usr/bin/python3
"""function that write a string in the file"""


def write_file(filename="", text=""):
    """
    write into file by creating
    or ovewriting the existing one
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
