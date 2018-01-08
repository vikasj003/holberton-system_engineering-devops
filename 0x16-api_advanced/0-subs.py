#!/usr/bin/python3
"""api subscribers"""
import json
import requests
import sys


def number_of_subscribers(subreddit):
    """subscribers"""
    subreddit = sys.argv[1]
    #API call to reddit URL
    url = "https://www.reddit.com/r/" + subreddit + "/about/.json"
    #response object called "info_request" all info will be grabbed from this obj
    info_request = requests.get(url, headers={'User-Agent': '118'})
    
    #to get keys in the "info_request" object
    data = info_request.json().get("data")
    subscribers = data.get("subscribers")
    #If not a valid subreddit, return 0
    if subscribers is None:
        subscribers = 0
    return(subscribers)
