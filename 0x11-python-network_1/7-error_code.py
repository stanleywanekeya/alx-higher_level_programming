#!/usr/bin/python3
"""request site and handles errors"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    t = requests.get(url)
    if t.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(t.text)
