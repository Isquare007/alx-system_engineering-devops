#!/usr/bin/python3
"""Reddit API"""
import re
from collections import Counter
from requests import get


def count_words(subreddit, word_list, after='', count=Counter()):
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {
            "limit": 100,
            "after": after
            }
    response = get(url, headers={'User-Agent': 'MyBot/0.0.1'}, params=params)
    if response.status_code == 200:
        data = response.json()
        for post in data['data']['children']:
            title = post['data']['title'].lower()
            for word in word_list:
                count[word] += len(
                    re.findall(
                        f'(?<![._]){word}(?![._])',
                        title))
        after = data['data']['after']
        if after:
            count_words(subreddit, word_list, after, count)
        else:
            if count:
                for word, count in count.most_common():
                    if count == 0:
                        continue
                    print(word, count)
    else:
        return
