#!/usr/bin/python3
"""Queries Reddit API and returns total subscribers for a subreddit."""

import requests


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "0-subs-script:v1.0 (by /u/your_username)"}
    try:
        resp = requests.get(url, headers=headers, allow_redirects=False, timeout=10)
        if resp.status_code != 200:
            return 0
        data = resp.json()
        return data.get("data", {}).get("subscribers", 0)
    except (requests.RequestException, ValueError):
        return 0


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Please pass a subreddit name.")
    else:
        print(number_of_subscribers(sys.argv[1]))
