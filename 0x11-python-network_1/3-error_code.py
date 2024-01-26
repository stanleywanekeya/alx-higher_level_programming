#!/usr/bin/python3
"""sends a get request and handles error"""


if __name__ == "__main__":
    form urllib import request, error
    import sys

    url = sys.argv[1]
    urllib.request.Request(url)
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode("utf-8"))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
