#!/usr/bin/python3
""" This script queries the Reddit API and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """ queries the Reddit API and returns the number of subscribers"""

    res = requests.get("https://www.reddit.com/r/{}/about.json"
                       .format(subreddit))
    if res.status_code >= 300:
        return 0

    return res.json().get("data").get("subscribers")
