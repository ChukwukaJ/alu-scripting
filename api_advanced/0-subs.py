#!/usr/bin/python3
"""
Module for getting subscriber count from Reddit API.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Get the number of subscribers for a subreddit.
    """
    if not subreddit or not isinstance(subreddit, str):
        return 0

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "python:alu-scripting:v1.0"}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            return 0
        data = response.json()
        return data.get("data", {}).get("subscribers", 0)
    except Exception:
        return 0
