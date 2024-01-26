#!/usr/bin/python3
"""Fetches the content id"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    t = requests.get(url)
    print(t.headers.get("X-Request-Id"))
