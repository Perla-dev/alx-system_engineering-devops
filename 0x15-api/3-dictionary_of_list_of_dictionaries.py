#!/usr/bin/python3
"""Exports to-do list information of all employees to JSON format"""
import requests
import json
import sys

if __name__ == "__main__":

    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    users_response = requests.get(users_url)
    todos_response = requests.get(todos_url)

    if users_response.status_code != 200:
        print("Error: Unable to fetch user data")
        sys.exit(1)

    if todos_response.status_code != 200:
        print("Error: Unable to fetch todos data")
        sys.exit(1)

    users = users_response.json()
    todos = todos_response.json()

    user_tasks = {}

    for user in users:
        user_id = user.get("id")
        employee_name = user.get("name")
        user_todos = [todo for todo in todos if todo.get("userId") == user_id]

        task_list = [{
            "username": employee_name,
            "task": todo.get("title"),
            "completed": todo.get("completed")
        } for todo in user_todos]

        user_tasks[user_id] = task_list

    with open('todo_all_employees.json', 'w') as jsonfile:
        json.dump(user_tasks, jsonfile)

    print("Data exported to todo_all_employees.json")
