#!/usr/bin/python3
"""
takes a URL, sends a request, and displays the X-Request-Id
"""

import urllib.request
from sys import argv

req = urllib.request.Request(argv[1])

with urllib.request.urlopen(req) as response:
    headers = dict(response.info())
    print(headers.get('X-Request-Id'))
