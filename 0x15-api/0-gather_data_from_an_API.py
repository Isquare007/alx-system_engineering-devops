#!/usr/bin/python3
"""
a script that returns info about a customer's todo list
"""
import requests
from sys import argv


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com"
    employeeId = argv[1]

    employee = requests.get("{}/users/{}".format(url, employeeId)).json()
    todos = requests.get(url + "/todos", params={"userId": employeeId}).json()

    done_task = []
    for data in todos:
        if data.get('completed') is True:
            done_task.append(data.get('title'))

    employee_name = employee.get('name')
    tasks_done_length = len(done_task)
    tasks_length = len(todos)

    print("Employee {} is done with tasks({}/{}):".format(employee_name, tasks_done_length, tasks_length))

    for title in done_task:
        print("\t {}".format(title))

