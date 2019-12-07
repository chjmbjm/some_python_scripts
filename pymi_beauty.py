#!/usr/bin/env python3
__doc__ == '''
Write a script to get 50 beauty spa/ hair salon in radius of 2km from
PyMi class.

Use Google Map API: https://developers.google.com/places/web-service/

Write result in file pymi_beauty.geojson and load to github.com to see
the map.

Enter your path to export geojson file. If path is not given or not correct,
file is saved to the current directory of the script.

Command: python3 pymi_beauty.py PATH
'''


import json
import requests
import sys
import os
import time

# You can create your own key token on console.cloud.google.com
ACCESS_KEY = 'AIzaSyB32P7edn96n3y2LZ1GZa0WkKYw7Sgyu-Y'

URL = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'

# You can change to your location
LOCATION = '21.013171,105.822266'

# You can your searching range
RADIUS = 2000

# You can change your key words
KEYWORDS = 'spa|hair+salon'


def get_places(path):
    places = []

    url = URL

    params = {
        'location': LOCATION,
        'radius': RADIUS,
        'keyword': KEYWORDS,
        'key': ACCESS_KEY
    }

    # Get data from google map api
    response = requests.get(url, params=params).json()
    places.extend(response['results'])
    while 'next_page_token' in response:
        time.sleep(10)
        params.update({'pagetoken': response['next_page_token']})
        next_response = requests.get(url, params=params).json()
        if len(places) > 50 or 'error_message' in next_response:
            break
        places.extend(next_response['results'])

    # Save places to file
    file_content = {
        'type': 'FeatureCollection',
        'features': [
            {
                'type': 'Feature',
                'geometry': {
                    'type': 'Point',
                    'coordinates': [
                        float(place['geometry']['location']['lng']),
                        float(place['geometry']['location']['lat'])
                    ]
                },
                'properties': {
                    'Address': place['vicinity'],
                    'name': place['name']
                }
            } for place in places]}

    save_path = os.path.join(path, 'pymi_beauty.geojson')
    with open(save_path, 'wt') as handle:
        json.dump(file_content, handle, ensure_ascii=False, indent=4)

    message = 'Found {} places'.format(len(places))

    return message


def main():
    path = ''
    if len(sys.argv) == 1:
        print('File is saved to current directory.')
        path = os.path.dirname(sys.argv[0])
    else:
        path = sys.argv[1]
        if os.path.exists(path) and os.path.isdir(path):
            print('File is saved on path: {}'.format(path))
        else:
            print('The given path does not work.')
            print('File is saved to current directory.')
            path = os.path.dirname(sys.argv[0])

    message = get_places(path)

    print(message)


if __name__ == '__main__':
    main()
