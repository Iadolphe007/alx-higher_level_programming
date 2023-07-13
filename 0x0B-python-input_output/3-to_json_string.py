#!/usr/bin/python3
"""return to JSON"""
import json


def to_json_string(my_obj):
    """
    serialize the string with
    JSON representation
    """
    return json.dumps(my_obj)
