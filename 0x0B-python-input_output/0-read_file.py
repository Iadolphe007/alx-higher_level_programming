#!/usr/bin/python3
"""Read text file"""


def read_file(filename=""):
    """read file and print it"""
    with open(filename, "r", encoding="utf-8") as f:
        read_file = f.read()
        print(read_file)
