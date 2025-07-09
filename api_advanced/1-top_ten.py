#!/usr/bin/python3
"""
1-top_ten module
Queries the Reddit API and prints titles of the top 10 hot posts for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Prints the titles of the top 10 hot posts from a subreddit.
    If the subreddit is invalid or there's an error, prints 'None'.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        "User-Agent": "python:alu-scripting:v1.0 (by /u/ChukwukaJ)"
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

        posts = response.json().get("data", {}).get("children", [])
        if not posts:
            print("None")
            return

        for post in posts:
            title = post.get("data", {}).get("title")
            if title:
                print(title)

    except Exception:
        print("None")
