#!/usr/bin/python3
"""
Module for getting subscriber count from Reddit API.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Get the number of subscribers for a subreddit.
    
    Args:
        subreddit (str): The subreddit name
        
    Returns:
        int: Number of subscribers or 0 if invalid
    """
    if not subreddit or not isinstance(subreddit, str):
        return 0
    
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "python:alu-scripting:v1.0"
    }
    
    try:
        response = requests.get(
            url,
            headers=headers,
            allow_redirects=False,
            timeout=10
        )
        
        if response.status_code != 200:
            return 0
            
        data = response.json()
        subscribers = data.get("data", {}).get("subscribers", 0)
        
        return subscribers if isinstance(subscribers, int) else 0
        
    except (requests.RequestException, ValueError, KeyError):
        return 0
