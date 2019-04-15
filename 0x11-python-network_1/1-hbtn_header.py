#!/usr/bin/python3
"""
takes a URL, sends a request, and displays the X-Request-Id
"""

import sys
import urllib.request

req = urllib.request.Request(sys.argv[1])

with urllib.request.urlopen(req) as response:
    meta_info = dict(response.info())
    print(meta_info.get('X-Request-Id'))
