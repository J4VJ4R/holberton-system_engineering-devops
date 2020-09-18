#!/usr/bin/python3
"""
function that queries the Reddit API and \
prints the titles of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts for a given subreddit."""

    url = 'https://api.reddit.com/r/{}/hot?limit=10'.format(subreddit)

    headers = {'user-agent': 'request-ae'}
    request = requests.get(url, headers=headers, allow_redirects=False)

    if request.status_code == 200:
        json_request = request.json().get('data')['children']

        for post in json_request:
            title = post.get('data')['title']
            print(title)
    else:
        print('None')
