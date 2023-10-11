#!/usr/bin/python3
"""
Write a function that queries the Reddit API and returns the number of subscribers (not active users, total subscribers) for a given subreddit. If an invalid subreddit is given, the function should return 0.
"""
import requests

def number_of_subscribers(subreddit):
    # Set a custom User-Agent to avoid Reddit API restrictions
    headers = {'User-Agent': 'MyRedditBot/1.0'}

    # URL for the Reddit API to get information about a subreddit
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    # Send an HTTP GET request to the Reddit API
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        # Extract the number of subscribers from the response
        subscribers = data['data']['subscribers']
        return subscribers
    elif response.status_code == 404:
        # If the subreddit is not found, return 0
        return 0
    else:
        # Handle other errors
        print(f"Error: {response.status_code} - Unable to retrieve data for subreddit '{subreddit}'")
        return 0
