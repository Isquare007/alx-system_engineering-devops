#!/usr/bin/python3
"""REddit api"""

import requests
from sys import argv


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts
    listed for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    headers = {"User-Agent": "My Reddit API Client/1.0"}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        top = response.json()
        titles_ = top["data"]["children"]
        for title_ in titles_:
            print(title_["data"]["title"])
    else:
        print(None)
