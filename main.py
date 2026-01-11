import json
import os
from datetime import datetime

tasks = {}

if os.path.exists("tasks.json") == False:
    with open("tasks.json", "w") as jsonfile:
        json.dump(tasks, jsonfile, indent=4)
else:
    with open("tasks.json", "r") as jsonfile:
        tasks = json.load(jsonfile)

userinput = ""

while userinput != "exit":
    userinput = input()

    if userinput[:3].lower() == "add":
        if (len(list(tasks.keys())) > 0):
            taskID = list(tasks.keys())[-1]+1
        else:
            taskID = 1

        taskDescription = userinput[3:].strip().replace('"', "")
        creationTime = str(datetime.now())

        tasks[taskID] = {"description": taskDescription, "status": "todo", "createdAt": creationTime, "updatedAt": creationTime}

        with open("tasks.json", "w") as jsonfile:
            json.dump(tasks, jsonfile, indent=4)

        print("Task added successfully (ID: " + str(taskID) + ")")