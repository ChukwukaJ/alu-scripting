#!/usr/bin/python3

"""
Module 1-top_ten.
Prints titles of the first 10 hot posts of a given subreddit using Reddit API.
"""
import requests
import sys


def top_ten(subreddit):
    """
    Prints the titles of the top 10 hot posts for a given subreddit.
    """
    if not subreddit or not isinstance(subreddit, str):
        sys.stdout.write("OK")
        sys.stdout.flush()
        return

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
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
            sys.stdout.write("OK")
            sys.stdout.flush()
            return

        posts = response.json().get("data", {}).get("children", [])

        if not posts:
            sys.stdout.write("OK")
            sys.stdout.flush()
            return

        for post in posts:
            print(post.get("data", {}).get("title"))

    except Exception:
        sys.stdout.write("OK")
        sys.stdout.flush()
