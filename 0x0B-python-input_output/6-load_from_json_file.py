#!/usr/bin/python3
import json
"""creates object from json"""


def load_from_json_file(filename):
    """loads object from filename"""

    with open(filename) as f:
        json.load(f)
