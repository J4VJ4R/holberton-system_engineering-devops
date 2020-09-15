#!/usr/bin/python3
"""
Script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import json
import requests


if __name__ == "__main__":

    url_user = 'https://jsonplaceholder.typicode.com/users/'

    r_user = requests.get(url_user)
    json_user = r_user.json()

    data = {}
    for usr in json_user:

        usr_id = str(usr['id'])
        url = 'https://jsonplaceholder.typicode.com/todos?userId=' + usr_id
        r_task = requests.get(url)
        json_task = r_task.json()
        base = []

        for task in json_task:
            base.append({
                'username': usr['username'],
                'task': task['title'],
                'completed': task['completed']
                })

        data[usr['id']] = base

    with open('todo_all_employees.json', mode='w') as json_file:
        json.dump(data, json_file)
