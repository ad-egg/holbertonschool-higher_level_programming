#!/usr/bin/python3
"""
takes a letter and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter
"""

if __name__ == '__main__':
    import requests
    from sys import argv

    url = 'http://0.0.0.0:5000/search_user'

    if len(argv) > 1:
        letter = argv[1]
    else:
        letter = ""

    r = requests.post(url, data={'q': letter})

    try:
        json_bod = r.json()
        if len(json_bod) == 0:
            print("No result")
        else:
            print("[{}] {}".format(json_bod['id'], json_bod['name']))
    except ValueError:
        print("Not a valid JSON")
