#!/usr/bin/python3
import requests
""" recursivly getting hot topics """


def recurse(subreddit, hot_list=None, after=None):
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Reddit Agent"}

    response = requests.get(url, headers=headers, params=after)
    if response.status_code == 200:
        data = response.json()
        children = data["data"]["children"]

        for child in children:
            hot_list.append(child["data"]["title"])

        after = data["data"]["after"]
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    elif response.status_code == 404:
        return None
    else:
        return None
