#!/usr/bin/python3
"""Pulls from API converts to json file"""
import json
import requests


def export_all_to_json():
    """ Saves all users to json file"""
    users_and_tasks = {}

    # print("userDict: {}".format(userDict))

    userJson = requests.get(
        'https://jsonplaceholder.typicode.com/users').json()
    todosJson = requests.get(
        'https://jsonplaceholder.typicode.com/todos').json()

    user_info = {}
    for user in userJson:
        user_info[user['id']] = user['username']

    for task in todosJson:
        if users_and_tasks.get(task['userId'], False) is False:
            print("user added: {}".format(task['userId']))
            users_and_tasks[task['userId']] = []
        task_dict = {}
        task_dict['username'] = user_info[task['userId']]
        task_dict['task'] = task['title']
        task_dict['completed'] = task['completed']

        users_and_tasks[task['userId']].append(task_dict)

    # print("users_and_tasks")
    with open("todo_all_employees.json", 'w') as jsonFile:
        json.dump(users_and_tasks, jsonFile)

    return 0

if __name__ == "__main__":
    export_all_to_json()

# Notes
# need all users --> make dict id:username
# get all todos
# loop the todos
# if user ID in task is not in dictionary ->
# add it with the value of an empty list
# if exists create new task dict with all info
# append the task dictionary to spec. user task list
# dump to file
