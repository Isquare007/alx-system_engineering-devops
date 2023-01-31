#!/usr/bin/python3
"""Reddit API call"""

import requests
from sys import argv


def number_of_subscribers(subreddit):
    """returns the number of subscribers (not active users,
    total subscribers)"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    headers = {"User-Agent": "My Reddit API Client/1.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if (response.status_code == 200):
        users = response.json()
        return users["data"].get("subscribers")
    else:
        return 0
