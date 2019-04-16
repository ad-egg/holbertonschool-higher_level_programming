#!/usr/bin/python3
"""
takes a URL, sends a request to the URL, then displays the status code
"""

if __name__ == '__main__':
    import requests
    from sys import argv

    url = argv[1]

    r = requests.get(url)
    if r.status_code == 200:
        print(r.text)
    else:
        print("Error code: {}".format(r.status_code))
