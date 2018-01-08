#!/usr/bin/python3
"""api subscribers"""


import requests
import sys


def top_ten(subreddit):
    """subscribers"""
    subreddit = sys.argv[1]
    headers = {'user-agent': 'TankorSmash'}
    """API call to reddit URL"""
    url = "https://www.reddit.com/r/" + subreddit + "/hot.json?limit=10"
    """response object called "info_request" all info will be grabbed"""
    request = requests.get(url, headers=headers)
    """If not a valid subreddit, print None"""
    if not request:
        print("None")
    else:
        data = request.json().get("data").get("children")
        """If not a valid subreddit, print None"""
        if not data:
            print("None")
        for child in data:
            """loop through to get top ten"""
            print(child.get("data").get("title"))
