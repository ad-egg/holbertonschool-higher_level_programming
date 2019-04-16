#!/usr/bin/python3
"""
takes a URL, sends a request to that URL, then displays the value of the
X-Request-Id variable in the response header
"""

if __name__ == '__main__':
    import requests
    from sys import argv

    url = argv[1]

    r = requests.get(url)
    if 'X-Request-Id' in r.headers:
        print(r.headers.get('X-Request-Id'))
