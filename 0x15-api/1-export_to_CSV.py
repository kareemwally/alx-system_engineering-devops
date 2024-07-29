#!/usr/bin/python3
"""
sending requests to the test API https://jsonplaceholder.typicode.com/
then storing them in a CSV file
    using requests , csv module
"""
if __name__ == "__main__":

    import csv
    import requests
    import sys

    user_id = sys.argv[1]
    filename = "{}.csv".format(user_id)
    fields = ['userId', 'user_name', 'completed', 'title']

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
        req = requests.get('https://jsonplaceholder.typicode.com/todos',
                           params={"userId": user_id})
        to_do = req.json()
        for task in to_do:
            del task['id']
            task["user_name"] = str(user_name)
        return to_do

    to_do = getting_titles()

    with open(filename, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields,
                                quoting=csv.QUOTE_ALL)
        writer.writerows(to_do)
