#!/usr/bin/python3
"""
a script that returns info about a customer's todo list
"""
import json
import requests
from sys import argv

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com"
    employeeId = argv[1]

    employee = requests.get(
        "{}/users/{}".format(url, employeeId)).json()
    todos = requests.get(
        "{}/todos".format(url),
        params={
            "userId": employeeId},).json()


    userName = employee.get('username')

    json_list = [{'task': data.get("title"), "completed": data.get(
            "completed"), "username": userName} for data in todos]

    json_f = {}
    json_f[employeeId] = json_list
    filename = "{}.json".format(employeeId)

    with open(filename, 'w') as f:
        json.dump(json_f, f)
