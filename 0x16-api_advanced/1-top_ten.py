#!/usr/bin/python3
""" Queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit."""
import requests


def top_ten(subreddit):
    """ queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit."""

    res = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10"
                       .format(subreddit))
    if res.status_code >= 300:
        print('None')
    else:
        for child in res.json().get("data").get("children"):
            print(child.get('data').get('title'))
