#!/usr/bin/python3
"""Sends a post request"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email", sys.argv[2]}

    t = requests.post(url, data=value)
    print(t.text)
