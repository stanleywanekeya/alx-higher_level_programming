#!/usr/bin/python3
import shutil
import sys

file = sys.argv[1]
with open(file) as fl:
    with open("copy.txt", "w") as cp:
        shutil.copyfileobj(fl, cp)
