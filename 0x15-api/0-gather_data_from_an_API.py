#!/usr/bin/python3
"""Python script that, for a given employee ID, returns information """
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    emp_id = int(argv[1])
    users = requests.get(url + "/users/{}".format(emp_id))
    name = users.json().get('name')
    todos = requests.get(url + '/todos')
    comp = 0
    num_todo = 0
    for todo in todos.json():
        if todo.get('userId') == int(emp_id):
            num_todo += 1
            if todo.get('completed'):
                comp += 1
    print('Employee {} is done with tasks({}/{}):'
          .format(name, comp, num_todo))
    print('\n'.join(["\t " + todo.get('title') for todo in todos.json()
          if todo.get('userId') == emp_id and todo.get('completed')]))
