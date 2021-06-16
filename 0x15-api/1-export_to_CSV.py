#!/usr/bin/python3
"""Pulls from API converts to csv file"""

import csv
import requests
import sys


def save_tasks_to_csv(empID):
    """ Saves tasks to CSV"""
    username = ''
    allTasks = []

    userRes = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(empID))
    todosRes = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.format(empID))

    username = userRes.json().get('username')
    todosJson = todosRes.json()

    for task in todosJson:
        taskRow = []
        taskRow.append(empID)
        taskRow.append(username)
        taskRow.append(task.get("completed"))
        taskRow.append(task.get("title"))

        allTasks.append(taskRow)

    # print("alltasks: {}".format(allTasks))

    with open("{}.csv".format(empID), 'w') as csvFile:
        csvwriter = csv.writer(csvFile, quoting=csv.QUOTE_ALL)
        csvwriter.writerows(allTasks)

    return 0

if __name__ == "__main__":
    save_tasks_to_csv(sys.argv[1])
# Notes
# WOAH! a file --> CSV (value,value,...)
# open and write
# specific file (ID.csv)
# all tasks for users -->

# to use the CSV module
# need to loop all the tasks and ad to list
# open the file
# csvwriter = csv.write(ourfile, quoting=csv.WUOTE_ALL)
# csvwriter.writerows(taskList)
