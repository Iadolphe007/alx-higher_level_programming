#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        sentence[0] = None
    else:
        i = len(sentence)
        fst_char = sentence[0]
        return (i, fst_char)
