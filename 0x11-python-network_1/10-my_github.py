#!/usr/bin/python3
"""log in to github and get the id of your account"""
import requests
import sys
from requests.auth import HTTPBasicAuth


if __name__ == "__maine__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    t = requests.get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))
