#!/usr/bin/env python3
def islower(c):
    for lowercase in range(97, 123):
        if chr(lowercase) == c:
            return True
    for uppercase in range(65, 91):
        if chr(uppercase) == c:
            return False
    return False

