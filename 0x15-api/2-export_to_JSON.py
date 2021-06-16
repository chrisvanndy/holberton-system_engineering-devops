#!/usr/bin/python3
"""Pulls from API converts to csv file"""
import json
import requests
import sys


def export_to_json(empID):
    """ Saves tasks to CSV"""
    username = ''
    userDict = {}

    # print("userDict: {}".format(userDict))

    userRes = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(empID))
    todosRes = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.format(empID))

    username = userRes.json().get('username')
    todosJson = todosRes.json()

    userDict[empID] = []

    for task in todosJson:
        taskDict = {}
        taskDict["task"] = task.get('title')
        taskDict["username"] = username
        taskDict["completed"] = task.get('completed')

        userDict[empID].append(taskDict)

    with open("{}.json".format(empID), 'w') as jsonFile:
        json.dump(userDict, jsonFile)

    return 0

if __name__ == "__main__":
    export_to_json(sys.argv[1])
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
