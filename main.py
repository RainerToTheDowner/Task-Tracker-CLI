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
    wordsInUserInput = userinput.split()
    command = wordsInUserInput[0].lower()

    if command == "add":
        if (len(list(tasks.keys())) > 0):
            taskID = int(list(tasks.keys())[-1])+1
        else:
            taskID = 1

        taskDescription = userinput[3:].strip().replace('"', "")
        creationTime = str(datetime.now())

        tasks[taskID] = {"description": taskDescription, "status": "todo", "createdAt": creationTime, "updatedAt": creationTime}

        with open("tasks.json", "w") as jsonfile:
            json.dump(tasks, jsonfile, indent=4)

        print("Task added successfully (ID: " + str(taskID) + ")")
    elif command == "update":
        possibleID = None
        possibleNewName = None
        if len(wordsInUserInput) > 2:
            possibleID = wordsInUserInput[1]
            possibleNewName = (" ".join(wordsInUserInput[2:])).replace('"', "")
        try:
            tasks[possibleID]["description"] = possibleNewName
            with open("tasks.json", "w") as jsonfile:
                json.dump(tasks, jsonfile, indent=4)
            print("Updated ID " + possibleID + ' to "' + possibleNewName + '"')
        except:
            print("ID does not exist or no name was given")