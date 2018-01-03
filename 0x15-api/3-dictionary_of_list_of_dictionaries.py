#!/usr/bin/python3
"""Write a Python script that, using this REST API"""
import json
import requests


def dictionary(username, task, complete):
    dict = {}
    dict['username'] = username
    dict['task'] = task
    dict['completed'] = complete
    return dict


if __name__ == "__main__":
    url_user = 'https://jsonplaceholder.typicode.com/users/'
    url_todos = 'https://jsonplaceholder.typicode.com/todos?userId='

    employee_req = requests.get(url_user)
    employee = employee_req.json()

    todos_req = requests.get(url_todos)
    todos = todos_req.json()

    employee_dict = {}
    for item in employee:
        employee_dict[item['id']] = item['username']

    todo_dict = {}

    for key in employee_dict:
        item_list = []
        for item in todos:
            if item['userId'] == key:
                item_list.append(dictionary(
                    employee_dict.get(key),
                    item.get('completed'),
                    item.get('title')))
        todo_dict[key] = item_list
    file_name = "todo_all_employees.json"
    with open(file_name, mode="w") as output:
        json.dump(todo_dict, output)
