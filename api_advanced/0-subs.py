#!/usr/bin/python3
"""
Module for querying Reddit API to get subscriber count.
This script fetches the number of subscribers for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Get the number of subscribers for a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit to query
        
    Returns:
        int: Number of subscribers, or 0 if subreddit is invalid
    """
    # Validate input
    if not subreddit or not isinstance(subreddit, str):
        return 0
    
    # Construct the API URL
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    # Set up headers to avoid rate limiting
    headers = {
        "User-Agent": "python:alu-scripting:v1.0 (by /u/student)"
    }
    
    try:
        # Make the API request without following redirects
        response = requests.get(
            url, 
            headers=headers, 
            allow_redirects=False, 
            timeout=10
        )
        
        # Check if request was successful
        if response.status_code != 200:
            return 0
            
        # Parse the JSON response
        data = response.json()
        subscribers = data.get("data", {}).get("subscribers", 0)
        
        # Return the subscriber count
        return subscribers if isinstance(subscribers, int) else 0
        
    except (requests.RequestException, ValueError, KeyError):
        # Handle any errors gracefully
        return 0
