#!/usr/bin/python3
"""
a simple function to get number of subs of subreddit
"""
import requests
import sys

client_id = "zg4h3mMKW60mJR1R7flA2Q"
secret = "Svjdt2c-7UHBqZ-90I3XpKdvWfTcqA"
auth = requests.auth.HTTPBasicAuth(client_id, secret)
data = {
        'grant_type': 'password',
        'username': 'Queasy-Regret2317',
        'password': ")%Fpdc$-!C%qE6A"
        }
headers = {'User-Agent': 'MyAPI'}
res = requests.post("https://www.reddit.com/api/v1/access_token",
                    auth=auth, data=data, headers=headers)
token = res.json()['access_token']
headers['Authorization'] = f'bearer {token}'


def number_of_subscribers(subreddit):
    """ a function to startsending requests to API"""
    test = requests.get('https://oauth.reddit.com/r/{}/about'
                        .format(subreddit), headers=headers)
    if test.status_code == 200:
        return (test.json()["data"]["subscribers"])
    else:
        return 0
