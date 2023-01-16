#!/usr/bin/python3
"""
a script that returns info about a customer's todo list
"""
import json
import requests
from sys import argv

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com"
    json_f = {}
    employee = requests.get(
        "{}/users".format(url)).json()
    for employ in employee:
        employeeId = employ.get('id')
        todos = requests.get("{}/todos".format(url), params={"userId": employeeId},).json()

        userName = employ.get('username')

        json_list = [{'username': userName, 'task': data.get("title"), "completed": data.get("completed")} for data in todos]

        json_f[employeeId] = json_list
    
    filename = "todo_all_employees" + ".json"

    with open(filename, 'w') as f:
        json.dump(json_f, f)
