#!/usr/bin/python3
"""
sending requests to the test API https://jsonplaceholder.typicode.com/
then storing them in a CSV file
    using requests , csv module
"""
if __name__ == "__main__":

    import json
    import requests
    import sys

    user_id = sys.argv[1]
    filename = "{}.json".format(user_id)
    fields = ['userId']

    def getting_username(link):
        """
        requests and responds from the test API to get username
        """
        res = requests.get('{}{}'.format(link, user_id))
        user_name = res.json().get("username")
        return user_name

    user_name = getting_username('https://jsonplaceholder.typicode.com/users/')

    def getting_titles():
        """
        obtaining titles, of the tasks
        """
        tmp = []
        d = {}
        req = requests.get('https://jsonplaceholder.typicode.com/todos',
                           params={"userId": user_id})
        to_do = req.json()
        for task in to_do:
            d = {"task": task.get("title"),
                 "completed": task.get("completed"),
                 "username": user_name}
            tmp.append(d)
        res = {"{}".format(user_id): tmp}
        return res

    to_do = getting_titles()

    with open(filename, 'w') as json_file:
        json.dump(to_do, json_file)
