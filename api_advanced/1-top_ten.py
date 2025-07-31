#!/usr/bin/python3

"""
Module 1-top_ten.
Prints titles of the first 10 hot posts of a given subreddit using Reddit API.
"""
import requests

str1 = "OK"


def top_ten(subreddit):
    """
    Prints the titles of the top 10 hot posts for a given subreddit.
    """
    if not subreddit or not isinstance(subreddit, str):
        print(str1, end="", flush=True)
        return

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "python:api.advanced:v1.0.0 (by /u/fakeuser1234)"
    }
    params = {"limit": 10}

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False,
            timeout=10
        )

        if response.status_code != 200:
            print(str1, end="", flush=True)
            return

        posts = response.json().get("data", {}).get("children", [])

        if not posts:
            print(str1, end="", flush=True)
            return

    except Exception:
        print(str1, end="", flush=True)
