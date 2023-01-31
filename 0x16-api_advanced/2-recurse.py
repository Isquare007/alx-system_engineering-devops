#!/usr/bin/python3
"""Redit API"""

import requests
from sys import argv


def recurse(subreddit, hot_list=[], after=None):
    """recursive function that returns a list containing the
    titles of all hot articles for a given subreddit"""
    subreddit = argv[1]
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {
        "limit": 100,
        "after": after
    }
    headers = {
        "User-Agent": "My Reddit API Client/1.0"
    }

    response = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        for post in data["data"]["children"]:
            hot_list.append(post["data"]["title"])
        after = data["data"]["after"]
        if after:
            return recurse(subreddit, hot_list, after)
        return hot_list
    else:
        return None
