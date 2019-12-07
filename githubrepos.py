#!/usr/bin/env python3

import requests
import sys
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
URL = 'https://api.github.com/users'


__doc__ == '''
Requirement:
Write a script to list all Github repos of input username.
Command: python3 githubrepos.py username
'''


def list_repos(input_data):
    result = []
    url_link = '{}/{}/{}'.format(URL, input_data, 'repos')

    r = requests.get(url_link)

    if r.status_code == 200:
        repos = r.json()
        result = [one['name'] for one in repos]

    return result


def main():
    if len(sys.argv) > 1:
        user = sys.argv[1]
        print(list_repos(user))
    else:
        print('No user is given.')


if __name__ == '__main__':
    main()
