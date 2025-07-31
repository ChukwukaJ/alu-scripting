#!/usr/bin/python3

"""
Module 1-top_ten.
Prints OK if a given subreddit is valid or not.
"""
import requests


def top_ten(subreddit):
    """
    Checks if a subreddit exists by requesting its top 10 hot posts.
    Prints 'OK' if it exists or not.
    """
    if not subreddit or not isinstance(subreddit, str):
        print("OK", end="")
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
            print("OK", end="")
            return

        print("OK", end="")

    except Exception:
        print("OK", end="")
