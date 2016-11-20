import json
import requests
from pprint import pprint


def api_get_request(url):
    # In this exercise, you want to call the last.fm API to get a list of the
    # top artists in Spain. The grader will supply the URL as an argument to
    # the function; you do not need to construct the address or call this
    # function in your grader submission.
    #
    # Once you've done this, return the name of the number 1 top artist in
    # Spain.

    data = requests.get(url).text
    data = json.loads(data)

    artists = data['topartists']['artist']
    # pprint(artists)

    for k in artists:
        if k['@attr']['rank'] == '1':
            return k['name']

    return -1  # return the top artist in Spain
