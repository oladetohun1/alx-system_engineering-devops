#!/usr/bin/python3
"""
A script that exports all tasks from all employees
in JSON format.

Usage:
    $ ./3-dictionary_of_list_of_dictionaries.py
"""

import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    users_url = f"{url}/users"
    todos_url = f"{url}/todos"

    # Retrieve user information
    users_data = requests.get(users_url).json()
    # Retrieve todos data
    todos_data = requests.get(todos_url).json()

    # Create a dictionary to store tasks for each user
    tasks_dict = {}
    for user in users_data:
        user_id = user.get('id')
        username = user.get('username')
        tasks = [
            {
                "username": username,
                "task": task.get('title'),
                "completed": task.get('completed')
            }
            for task in todos_data
            if task.get('userId') == user_id
        ]
        tasks_dict[user_id] = tasks

    # Export data to JSON file
    json_filename = "todo_all_employees.json"
    with open(json_filename, 'w') as json_file:
        json.dump(tasks_dict, json_file)
