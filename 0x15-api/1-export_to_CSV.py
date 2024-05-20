#!/usr/bin/python3
"""Script that extends 0-gather_data_from_an_API.py
to export data in the CSV format. """
import csv
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    user_id = int(sys.argv[1])
    user = requests.get(url + "/users/{}".format(user_id))
    todos = requests.get(url + '/todos')
    name = user.json().get('username')
    file_name = sys.argv[1] + '.csv'

    with open(file_name, mode='w') as f:
        writer = csv.writer(f, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL,
                            lineterminator='\n')
        for todo in todos.json():
            if todo.get('userId') == user_id:
                writer.writerow([user_id, name, str(todo.get('completed')),
                                todo.get('title')])
