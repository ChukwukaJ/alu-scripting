#!/usr/bin/python3
"""
Module 1-top_ten
Queries the Reddit API and prints the titles of the first 10 hot posts of a subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Prints the titles of the top 10 hot posts for a given subreddit.

    Args:
        subreddit (str): The subreddit name

    If subreddit is invalid or an error occurs, prints 'None'.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "python:api.advanced:v1.0.0 (by /u/fakeuser123)"
    }
    params = {
        "limit": 10
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False,
            timeout=10
        )
        if response.status_code != 200:
            print("None")
            return

        data = response.json().get("data", {})
        posts = data.get("children", [])

        for post in posts:
            title = post.get("data", {}).get("title")
            if title:
                print(title)

    except Exception:
        print("None")
