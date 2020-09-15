#!/usr/bin/python3
"""
Script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
from sys import argv


if __name__ == "__main__":

    user_id = argv[1]

    url_user = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    url_todos = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
        user_id)

    r_user = requests.get(url_user)
    r_todos = requests.get(url_todos)
    json_user = r_user.json()
    json_todos = r_todos.json()
    done_tasks = 0
    total_tasks = len(json_todos)
    employee_name = json_user['name']

    for task in json_todos:
        if task['completed'] is True:
            done_tasks += 1

    print('Employee {} is done with tasks({}/{}):'.format(employee_name,
                                                          done_tasks,
                                                          total_tasks))

    for task in json_todos:
        if task['completed'] is True:
            print('\t {}'.format(task['title']))
