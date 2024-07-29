#!/usr/bin/python3
""" sending requests to the test API https://jsonplaceholder.typicode.com/
    using requests module
"""
if __name__ == "__main__":

    import requests
    import sys

    user_id = sys.argv[1]

    def tasks_done(to_do):
        """ getting the number of achieved tasks"""
        res = 0
        for task in to_do:
            if task["completed"]:
                res += 1
        return res, len(to_do)

    def snd_requests(link):
        """ requests and responds from the test API"""
        res = requests.get('{}{}'.format(link, user_id))
        return res

    def print_titles(to_do):
        """ printing titled of th achieved tasks"""
        for task in to_do:
            if task["completed"]:
                print("\t {}".format(task.get("title")))

    res = snd_requests('https://jsonplaceholder.typicode.com/users/')

    user_name = res.json().get("name")

    req = requests.get('https://jsonplaceholder.typicode.com/todos',
                       params={"userId": user_id})

    to_do = req.json()
    print("Employee {0} is done with tasks({1}/{2}):"
          .format(user_name, tasks_done(to_do)[0], tasks_done(to_do)[1]))

    print_titles(to_do)
