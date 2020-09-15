#!/usr/bin/python3
"""
Script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
from sys import argv
import csv
import requests


if __name__ == "__main__":

    user_id = argv[1]

    url_user = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    url_todos = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
        user_id)

    r_user = requests.get(url_user)
    r_todos = requests.get(url_todos)
    json_user = r_user.json()
    json_todos = r_todos.json()
    employee_username = json_user['username']

    with open(user_id + '.csv', mode='w') as file:
        writer = csv.writer(file, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_ALL)

        for task in json_todos:
            writer.writerow([user_id, employee_username,
                            task['completed'], task['title']])
