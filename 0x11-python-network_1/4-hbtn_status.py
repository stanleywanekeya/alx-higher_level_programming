#!/usr/bin/pthon3
"""fetches the body of url"""
import requests


if __name__ == "__main__":
    response = requests.get("https://alx-intranet.hbtn.io/status")
    t = r.text
    print("Body response:\n\t- type: {}\n\t- content: {}".format(type(t), t))
