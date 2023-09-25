#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format"""
import requests
import sys
import csv

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: {} <employee ID>".format(sys.argv[0]))
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(employee_id)

    response = requests.get(user_url)
    if response.status_code != 200:
        print("Error: Unable to fetch user data")
        sys.exit(1)

    user = response.json()
    employee_name = user.get("name")

    response = requests.get(todos_url)
    if response.status_code != 200:
        print("Error: Unable to fetch todos data")
        sys.exit(1)

    todos = response.json()
    done_tasks = [task for task in todos if task.get("completed") == True]

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(done_tasks), len(todos)))
    for task in done_tasks:
        print("\t {}".format(task.get("title")))

    with open('{}.csv'.format(employee_id), 'w', newline='') as csvfile:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for task in todos:
            writer.writerow({
                "USER_ID": employee_id,
                "USERNAME": employee_name,
                "TASK_COMPLETED_STATUS": task.get("completed"),
                "TASK_TITLE": task.get("title")
            })

    print("Data exported to {}.csv".format(employee_id))
