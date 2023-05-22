#!/usr/bin/python3
"""
A script that returns information about an employee TODO list
progress, given its ID and exports its data in JSON format.

Usage:
    $ ./2-export_to_JSON.py <employee_id>
"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    """
    The script must accept an integer as a parameter,
    which is the employee ID
    """
    if len(argv) != 2:
        print('''
        Only two arguments expected:
        $ ./2-export_to_JSON.py <employee_id>
        ''')
        exit(1)
    employee_id = int(argv[1])
    url = "https://jsonplaceholder.typicode.com"
    employee_url = f"{url}/users/{employee_id}"
    todos_url = f"{url}/todos?userId={employee_id}"

    # Retrieve employee information
    employee_data = requests.get(employee_url).json()
    # Retrieve employee's todo lists
    todo_data = requests.get(todos_url).json()
    # Retrieve other relevant data
    employee_username = employee_data.get('username')
    tasks = [
        {
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": employee_username
        }
        for task in todo_data
    ]
    json_data = {employee_id: tasks}

    # Export data to JSON file
    json_filename = f"{employee_id}.json"
    with open(json_filename, 'w') as json_file:
        json.dump(json_data, json_file)

    print(f"Data exported to {json_filename} successfully.")
