#!/usr/bin/python3
"""Reddit API"""
from collections import Counter
import re
from requests import get


def count_words(subreddit, word_list, after='', count=Counter()):
    """ recursive function that queries the Reddit API """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {
        "limit": 100,
        "after": after
    }
    response = get(url, headers={'User-Agent': 'MyBot/0.0.1'}, params=params)
    if after is None:
        word_list = [word.lower() for word in word_list]
    if response.status_code == 200:
        data = response.json()
        for post in data['data']['children']:
            for word in word_list:
                count[word] += len(
                    re.findall(
                        "(?<![._]){}(?![._])".format(word),
                        title))
        after = data['data']['after']
        if after:
            count_words(subreddit, word_list, after, count)
        else:
            if count:
                for word, count in count.most_common():
                    if count == 0:
                        continue
                    print("{}: {}".format(word, count))
    else:
        return
