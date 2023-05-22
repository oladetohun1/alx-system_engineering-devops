#!/usr/bin/python3
"""A script that returns information about an employee TODO list progress, given its ID.  
"""

import requests
from sys import argv


if __name__ == "__main__":
    """The script must accept an integer as a parameter, which is the employee ID
    """
    if len(argv) != 2:
        print('''
        Only two arguments expected :
        $ ./0-gather_data_from_an_API.py <employee_id>''')
        exit(1)
    id = argv[1]
    url = "https://jsonplaceholder.typicode.com"
    employee_url = f"{url}/users/{id}"
    todos_url = f"{url}/todos?userId={id}"

    # Retrieve employee information
    employee_data = requests.get(employee_url).json()
    # retrive employee todo lists
    todo_data = requests.get(todos_url).json()
    # retrieve other relevant data
    employee_name = employee_data['name']
    completed_tasks = [task['title'] for task in todo_data if task['completed']]
    num_of_done_tasks = len(completed_tasks)
    total_number_of_tasks = len(todo_data)
    # print the required output
    print(f"Employee {employee_name} is done with tasks({num_of_done_tasks}/{total_number_of_tasks}):")
    for task in completed_tasks:
        print("\t{}".format(task))
