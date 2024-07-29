#!/usr/bin/python3
"""
Script to export tasks data for all users in JSON format using requests module.
"""
import json
import requests


def fetch_users():
    """
    Fetch the details of all users from the API.
    """
    url = 'https://jsonplaceholder.typicode.com/users'
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad status codes
    return response.json()


def fetch_tasks():
    """
    Fetch all tasks from the API.
    """
    url = 'https://jsonplaceholder.typicode.com/todos'
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad status codes
    return response.json()


def format_data(users, tasks):
    """
    Format the data into the required JSON structure.
    """
    data = {}
    for user in users:
        user_id = str(user["id"])
        username = user["username"]
        user_tasks = [
            {"username": username, "task": task["title"],
             "completed": task["completed"]}
            for task in tasks if task["userId"] == user["id"]
        ]
        data[user_id] = user_tasks
    return data


def save_to_json(filename, data):
    """
    Save the formatted data to a JSON file.
    """
    with open(filename, 'w') as json_file:
        json.dump(data, json_file)


if __name__ == "__main__":
    try:
        users = fetch_users()
        tasks = fetch_tasks()
        data = format_data(users, tasks)
        filename = "todo_all_employees.json"
        save_to_json(filename, data)
        print(f"Data for all users saved to {filename}")

    except requests.exceptions.RequestException as e:
        print(f"HTTP Request failed: {e}")
        sys.exit(1)

    except ValueError as e:
        print(f"Error processing JSON data: {e}")
        sys.exit(1)
