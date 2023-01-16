#!/usr/bin/python3
"""
a script that returns info about a customer's todo list
"""
import csv
import requests
from sys import argv

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com"
    employeeId = argv[1]

    employee = requests.get(
        "{}/users/{}".format(url, employeeId), verify=False).json()
    todos = requests.get(
        "{}/todos".format(url),
        params={
            "userId": employeeId},
        verify=False).json()

    done_task = []
    for data in todos:
        if data.get('completed') is True:
            done_task.append(data.get('title'))

    userName = employee.get('username')

    csv_list = []
    for data in todos:
        csv_list.append([employeeId, userName, data.get(
            "completed"), data.get("title")])

    filename = "{}.csv".format(employeeId)

    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(
            csvfile,
            delimiter=',',
            quotechar='"',
            quoting=csv.QUOTE_ALL)

        for line in csv_list:
            csvwriter.writerow(line)
