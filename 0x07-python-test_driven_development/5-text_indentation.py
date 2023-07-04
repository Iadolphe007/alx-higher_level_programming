#!/usr/bin/python3
""" print text with special character """


def text_indentation(text):
    """
     prints a text with 2 new lines after each of these characters: ., ? and :

     Args:
        text(string): type to print
    Raises:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while i < len(text) and text[i] == ' ':
        i += 1
    while i < len(text):
        print(text[i], end="")
        special = ['.', '?', ':']
        if text[i] == "\n" or text[i] in special:
            if text[i] in special:
                print("\n")
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1
