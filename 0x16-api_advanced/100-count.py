#!/usr/bin/python3
"""Reddit API"""
from collections import Counter
import re
from requests import get


def count_words(subreddit, word_list, after='', found_word=[]):
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
            title = post['data']['title'].lower()
            for word in title.split(' '):
                if word in word_list:
                    found_word.append(word)

            """for word in word_list:
                count[word] += len(
                    re.findall(
                        "(?<![._]){}(?![._])".format(word),
                        title))
        after = data['data']['after']"""
        after = data['after']
        if after:
            count_words(subreddit, word_list, after, found_word)
        else:
            """if count:
                for word, count in count.most_common():
                    if count == 0:
                        continue
                    print(word, count)"""
            result = {}
            for word in found_word:
                if word.lower() in result.keys():
                    result[word.lower()] += 1
                else:
                    result[word.lower()] = 1
            for key, value in sorted(
                    result.items(), key=lambda item: item[1], reverse=True):
                print("{}: {}".format(key, value))
    else:
        return
