#!/usr/bin/python3
"""Script that extends 0-gather_data_from_an_API.py
to export data in the JSON format. """
import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    users = requests.get(url + '/users/')
    todos = requests.get(url + '/todos')
    json_file = 'todo_all_employees.json'

    data = dict()
    for user in users.json():
        user_id = user['id']
        user_name = user['username']
        data[str(user_id)] = []
        for todo in todos.json():
            if todo.get('userId') == user_id:
                data[str(user_id)].append(
                    {
                        "username": user_name,
                        "task": todo['title'],
                        "completed": todo['completed']
                    }
                )

    with open(json_file, 'w', newline='') as f:
        json.dump(data, f)
