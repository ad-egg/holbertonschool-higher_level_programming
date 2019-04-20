#!/usr/bin/python3
"""
takes my Github credentials (username and password) and uses the Github API
to display my id
"""

if __name__ == '__main__':
    import requests
    from sys import argv

    usern = argv[1]
    passw = argv[2]

    r = requests.get('https://api.github.com/user', auth=(usern, passw))
    if r.status_code == 200:
        user_dict = r.json()
        print(user_dict['id'])
    else:
        print("None")
