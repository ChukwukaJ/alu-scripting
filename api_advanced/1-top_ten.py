#!/usr/bin/python3
"""
Returns titles of the first 10 hot posts from a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Returns a list of titles for the top 10 hot posts in a subreddit.
    If subreddit is invalid or an error occurs, return None.
    """
    if not subreddit or not isinstance(subreddit, str):
        return None

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
            return None

        data = response.json().get("data", {}).get("children", [])
        return [post["data"]["title"] for post in data]

    except Exception:
        return None
