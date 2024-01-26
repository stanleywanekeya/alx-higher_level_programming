#!/usr/bin/python3
"""List the commit messages in the github"""
import requests
import sys


if __name__ == "__main__":
    url = "http://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    t = requests.get(url)
    commits = t.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
