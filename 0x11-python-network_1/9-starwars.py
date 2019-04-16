#!/usr/bin/python3
"""
Takes a string and sends a search request to the Star Wars API
"""

if __name__ == '__main__':
    import requests
    from sys import argv

    search = argv[1]
    url = 'https://swapi.co/api/people/'

    r = requests.get(url, params={'search': search})

    r_body_dict = r.json()

    num_results = r_body_dict['count']
    print("Number of results: {:d}".format(num_results))

    if num_results > 0:
        for person in r_body_dict['results']:
            print(person['name'])
