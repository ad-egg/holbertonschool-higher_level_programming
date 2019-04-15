#!/usr/bin/python3
"""
takes a URL and email, sends a POST request to URL with email as a parameter,
displays the response
"""

if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    from sys import argv

    url = argv[1]
    email = argv[2]

    data = urllib.parse.urlencode({'email': email})
    data = data.encode('ascii')
    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        the_page = response.read()
        print(the_page.decode('utf-8'))
