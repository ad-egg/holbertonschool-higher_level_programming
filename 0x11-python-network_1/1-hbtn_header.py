#!/usr/bin/python3
"""
takes a URL, sends a request, and displays the X-Request-Id
"""

import urllib.request
from sys import argv

with urllib.request.urlopen(argv[1]) as response:
    headers = dict(response.info())
    print(headers.get('X-Request-Id'))
