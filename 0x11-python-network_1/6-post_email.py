#!/usr/bin/python3
"""
takes a URL and email address, sends a POST request to the URL with email as
parameter, then displays body of the response
"""

if __name__ == '__main__':
    import requests
    from sys import argv

    url = argv[1]
    email = argv[2]
    r = requests.post(url, data={'email': email})
    print(r.text)
