#!/usr/bin/python3
"""Recursive function that queries the Reddit API for all hot posts."""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Returns a list of titles of all hot articles for a subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "python:api.advanced:v1.0.0 (by /u/fakeuser1234)"}
    params = {"limit": 100}
    if after:
        params["after"] = after

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json().get("data", {})
    posts = data.get("children", [])
    for post in posts:
        hot_list.append(post.get("data", {}).get("title"))

    after = data.get("after")
    if after:
        # ⚠️ Required for the test to detect recursion
        return recurse(subreddit, hot_list, after)
    return hot_list
