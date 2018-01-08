#!/usr/bin/python3
"""api subscribers"""
import requests
import sys


def number_of_subscribers(subreddit):
    """subscribers"""
    subreddit = sys.argv[1]
    headers = {'user-agent': 'TankorSmash'}
    """API call to reddit URL"""
    url = 'https://www.reddit.com/r/' + subreddit + '/about.json'
    """response object called "info_request" all info will be grabbed"""
    info_request = requests.get(url, headers=headers)
    data = info_request.json().get("data")
    scribers = data.get("subscribers")
    """If not a valid subreddit, return 0"""
    if scribers is None:
        scribers = 0
    return(scribers)
