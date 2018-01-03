#!/usr/bin/python3
"""Write a Python script that, using this REST API"""
import sys
import json
import requests


if __name__ == "__main__":
    employee_id = sys.argv[1]
    url_user = 'https://jsonplaceholder.typicode.com/users/'

    task_id = sys.argv[1]
    url_todos = 'https://jsonplaceholder.typicode.com/todos?userId='

    #employee data request
    employee_req = requests.get(url_user + employee_id)
    employee = employee_req.json()

    #task todo request
    list_tasks = []
    
    todos_req = requests.get(url_todos + task_id)
    todos = todos_req.json()

    #grab each task and add to list
    for item in todos:
        if item.get('completed') is True:
            list_tasks.append(item.get('title'))

    number_tasks = len(list_tasks)
    total_tasks = len(todos)

    print("Employee {} is done with tasks({}/{}):".format
          (employee.get('name'), number_tasks, total_tasks))
    for item in list_tasks:
        print("\t" + item)


    
