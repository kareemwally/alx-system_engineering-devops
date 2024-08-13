#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of
    subscribers for a given subreddit.
    If an invalid subreddit is given, the function returns 0.
    """
    # Set the base URL and headers for the request
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent':
               'Custom User Agent for querying subreddit subscribers'}

    try:
        # Send the GET request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            # Return the number of subscribers
            return data['data']['subscribers']
        else:
            return 0
    except requests.RequestException:
        # Handle any request exceptions and return 0
        return 0
