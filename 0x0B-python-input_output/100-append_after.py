#!/usr/bin/python3
"""
 inserts a line of text to a file, after each
 line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """ insert a text after each line"""
    txt = ""
    with open(filename) as f:
        for ln in f:
            txt += ln
            if search_string in ln:
                txt += new_string
    with open(filename, "w") as w:
        w.write(txt)
