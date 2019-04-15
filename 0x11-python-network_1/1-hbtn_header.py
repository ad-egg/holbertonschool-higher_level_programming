#!/usr/bin/python3
"""
takes a URL, sends a request, and displays the X-Request-Id
"""

import urllib.request
from sys import argv

with urllib.request.Request(argv[1]) as req:
    with urllib.request.urlopen(req) as response:
        meta_info = dict(response.info())
        print(meta_info.get('X-Request-Id'))
