#!/usr/bin/python3
"""Write a Python script that, using this REST API"""
import json
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    url_user = 'https://jsonplaceholder.typicode.com/users/'
    employee_id = sys.argv[1]

    url_todos = 'https://jsonplaceholder.typicode.com/todos?userId='
    task_id = sys.argv[1]

    employee_req = requests.get(url_user + employee_id)
    employee = employee_req.json()
    username = employee.get('username')

    todos_req = requests.get(url_todos + task_id)
    todos = todos_req.json()
    csv_file = user_id + ".csv"

    for item in todos:
        complete = item.get('completed')
        title = item.get('title')
        with open(csv_file, "a+") as output:
            output.write('"{}","{}", "{}", "{}"\n'.format
                         (user_id, username, complete, title))
