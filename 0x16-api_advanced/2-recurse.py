#!/usr/bin/python3
""" This script has a recursive function that queries the Reddit API
and returns a list containing the titles of all hot articles
for a given subreddit."""

import requests


def recurse(subreddit, hot_list=[], count=0, after=None):
    """recursive function that queries the Reddit API
    and returns a list containing the titles
    of all hot articles for a given subreddit."""

    res = requests.get("https://www.reddit.com/r/{}/hot.json"
                       .format(subreddit),
                       headers={"User-Agent": "custom"},
                       params={"count": count, "after": after})

    if res.status_code >= 400:
        return None

    new_hot_list = hot_list
    for child in res.json().get("data").get("children"):
        new_hot_list.append(child.get("data").get("title"))

    if not res.json().get("data").get("after"):
        return new_hot_list

    return recurse(subreddit, new_hot_list,
                   res.json().get("data").get("count"),
                   res.json().get("data").get("after"))
