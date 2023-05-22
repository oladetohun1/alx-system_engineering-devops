#!/usr/bin/python3
"""
A script that returns information about an employee TODO list
progress, given its ID and exports its data in CSV format.

Usage:
    $ ./1-export_to_CSV.py <employee_id>
"""

import csv
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
        $ ./0-gather_data_from_an_API.py <employee_id>
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
    employee_id = employee_data.get('id')
    employee_username = employee_data.get('username')
    employee_name = employee_data.get('name')
    completed_tasks = [task for task in todo_data if task.get('completed')]

    # Prepare CSV data
    csv_data = [
        [employee_id, employee_username, task.get('completed'), task.get('title')]
        for task in completed_tasks
    ]

    # Export data to CSV file
    csv_filename = f"{employee_id}.csv"
    with open(csv_filename, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        csv_writer.writerows(csv_data)

    print(f"Data exported to {csv_filename} successfully.")
