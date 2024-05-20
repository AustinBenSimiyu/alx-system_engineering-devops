#!/usr/bin/python3
"""Script that extends 0-gather_data_from_an_API.py
to export data in the JSON format. """
import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    user_id = int(sys.argv[1])
    user = requests.get(url + "/users/{}".format(user_id))
    todos = requests.get(url + '/todos')
    name = user.json().get('username')
    json_file = sys.argv[1] + '.json'

    data = dict()
    data[str(user_id)] = []

    for todo in todos.json():
        if todo.get('userId') == user_id:
            data[str(user_id)].append(
                {
                    "task": todo['title'],
                    "completed": todo['completed'],
                    "username": name
                }
            )

    with open(json_file, 'w', newline='') as f:
        json.dump(data, f)
