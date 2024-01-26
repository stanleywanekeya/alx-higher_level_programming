#!/usr/bin/python3
import shutil
import tempfile
import urllib.request


with urllib.request.urlopen('http://www.python.org/') as response:
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        shitil.copyfileobj(response, tmp_file)

with open(tmp_file.name.name) as html:
    pass
