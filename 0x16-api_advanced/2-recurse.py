#!/usr/bin/python3
"""
A recursive function to get the hot posts of a subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recursively fetch the hot posts of a subreddit"""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    params = {'after': after} if after else {}

    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json().get('data', {})
    children = data.get('children', [])

    for child in children:
        hot_list.append(child['data']['title'])

    after = data.get('after')
    if after:
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list


# Example usage
if __name__ == "__main__":
    subreddit = 'programming'
    hot_posts = recurse(subreddit)
    if hot_posts:
        print(len(hot_posts))
        print(hot_posts)
    else:
        print("None")
