#!/usr/bin/python3
"""
a script that returns info about a customer's todo list
"""
import requests
from sys import argv
import csv

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com"
    employeeId = argv[1]

    employee = requests.get("{}/users/{}".format(url, employeeId)).json()
    todos = requests.get(url + "/todos", params={"userId": employeeId}).json()

    done_task = []
    for data in todos:
        if data.get('completed') is True:
            done_task.append(data.get('title'))

    userId = employee.get('id')
    
    csv_list = []
    for data in todos:
        csv_list.append([data.get("userId"), employee.get("username"), data.get("completed"), data.get("title")])

    filename = "{}.csv".format(userId)

    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

        for line in csv_list:
            csvwriter.writerow(line)
