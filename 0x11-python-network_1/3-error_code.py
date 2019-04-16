#!/usr/bin/python3
"""
takes a URL, sends request to that URL, then displays the body of the response
decoded in utf-8
"""

if __name__ == '__main__':
    from sys import argv
    import urllib.error
    import urllib.request

    url = argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            html = response.read()
            print(html.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
