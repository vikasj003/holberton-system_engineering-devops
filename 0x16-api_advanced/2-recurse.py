#!/usr/bin/python3
"""api subscribers"""


import requests
import sys


def recurse(subreddit, hot_list=[]):    
    """subscribers"""
    subreddit = sys.argv[1]
    headers = {'user-agent': 'TankorSmash'}
    """API call to reddit URL"""
    url = "https://www.reddit.com/r/" + subreddit + "/hot.json?limit=10"
    """response object called "info_request" all info will be grabbed"""
    request = requests.get(url, headers=headers)
