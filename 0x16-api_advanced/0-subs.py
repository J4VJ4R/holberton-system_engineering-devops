#!/usr/bin/python3
"""
function that queries the Reddit API and \
returns the number of subscribers for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers for a given subreddit."""

    url = 'https://api.reddit.com/r/{}/about'.format(subreddit)

    headers = {'user-agent': 'request-ae'}
    request = requests.get(url, headers=headers, allow_redirects=False)

    if request.status_code == 200:
        json_request = request.json().get('data')
        return json_request['subscribers']
    else:
        return 0
