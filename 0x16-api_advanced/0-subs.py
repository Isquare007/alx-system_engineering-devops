#!/usr/bin/python3
"""Reddit API call"""

from sys import argv
import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers (not active users,
    total subscribers)"""
    link = argv[1]
    url = "https://www.reddit.com/r/" + link + "/about.json"

    headers = {"User-Agent": "My Reddit API Client/1.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if (response.status_code == 200):
        users = response.json()
        return users["data"].get("subscribers")
    else:
        return 0
