#!/usr/bin/python3
"""returns python value from json"""


import json


def from_json_string(my_str):
    """converts from json back to python value"""

    return json.loads(my_str)
