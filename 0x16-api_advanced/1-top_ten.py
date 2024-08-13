#!/usr/bin/python3
"""
a simple function to get top 10 hot posts of a subreddit
"""
import requests

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


def top_ten(subreddit):
    """ a function to startsending requests to API"""
    test = requests.get('https://oauth.reddit.com/r/{}/hot'
                        .format(subreddit), headers=headers)
    if test.status_code == 200:
        res = []
        for post in test.json()["data"]["children"]:
            res.append(post["data"]["title"])
        for i in range(10):
            print(res[i])
    else:
        return 0
