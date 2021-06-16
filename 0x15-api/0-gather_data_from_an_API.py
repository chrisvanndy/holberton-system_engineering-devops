#!/usr/bin/python3
"""Module pulls API from web interface"""
import requests
import sys


def get_emp_tasks(empID):
    """ Gets employee Tasks"""
    # variables
    name = ''
    task_list = []
    completed = 0

    # do get requests
    userRes = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(empID))
    todosRes = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.format(empID))

    #print("userRes: {}\n".format(userRes))
    #print("todosRes: {}\n".format(todosRes))
    # get the json from responses
    name = userRes.json().get('name')
    #print("Name: {}".format(name))

    todosJson = todosRes.json()
    # save the employee name

    # loop the tasks
    for task in todosJson:
        if task.get('completed') is True:
            completed += 1
            task_list.append(task.get('title'))
    # up counter variable if tasks completed
    print("Employee {} is done with tasks({}/{}:)".format(
        name, completed, len(todosJson)))
    for task in task_list:
        print("\t {}".format(task))
    # save task titles to a task_list []

    # print the first line

    # loop the task_list and print tasks

    return 0

if __name__ == "__main__":
    get_emp_tasks(sys.argv[1])


# Write a python script that uses a REST API for a given empllyee ID
# and returns info about his/her todo list progress
# I think i need to use sys to get input from terminal
# Need to look at provided API
# - name, #tasks (done v. not), task titles
# DONT FORGET THE TAB AND SPACE IN OUTPUT
# look at requests module
