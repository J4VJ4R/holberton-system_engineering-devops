#!/usr/bin/python3
"""
function that queries the Reddit API and \
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """prints the titles of all hot posts listed for a given subreddit."""
    url = 'https://api.reddit.com/r/{}/hot?after={}'.format(subreddit, after)
    headers = {'User-Agent': 'request-ae'}
    r = requests.get(url, headers=headers, allow_redirects=False)

    if r.status_code == 200:

        json_content = r.json()
        after = json_content['data']['after']

        for top in json_content.get('data')['children']:
            hot_list.append(top['data']['title'])

        if after is not None:
            recurse(subreddit, hot_list, after)

        return hot_list

    else:
        return None
