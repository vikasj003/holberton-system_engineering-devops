#!/usr/bin/python3
"""Write a Python script that, using this REST API"""
import sys
import json
import requests


if __name__ == "__main__":
    url_user = 'https://jsonplaceholder.typicode.com/users/'
    employee_id = sys.argv[1]

    url_todos = 'https://jsonplaceholder.typicode.com/todos?userId='
    task_id = sys.argv[1]

    employee_req = requests.get(url_user + employee_id)
    employee = employee_req.json()
    username = employee.get('username')

    todos_req = requests.get(url_todos + task_id)
    todos = todos_req.json()

    file_name = sys.argv[1] + ".json"
    dictionary = {}
    json_dict = {}
    item_list = []
    for item in todos:
        complete = item.get('completed')
        title = item.get('title')
        dictionary.update(
            {"task": title, "completed": complete, "username": username})
        item_list.append(dictionary)
        json_dict = sys.argv[1]

        with open(file_name, mode="w") as output:
            json.dump(json_dict, output)
