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

def printTaskInfo(task):
    print("\nID: " + str(task[0]))
    print("Description: " + task[1]["description"])
    print("Status: " + task[1]["status"])
    print("Created at: " + task[1]["createdAt"])
    print("Last updated at: " + task[1]["updatedAt"])

userinput = ""

while userinput.lower() != "exit":
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

        tasks[str(taskID)] = {"description": taskDescription, "status": "todo", "createdAt": creationTime, "updatedAt": creationTime}

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
                tasks[possibleID]["updatedAt"] = str(datetime.now())
                with open("tasks.json", "w") as jsonfile:
                    json.dump(tasks, jsonfile, indent=4)
                print("Updated ID " + possibleID + ' to "' + possibleNewName + '"')
            except:
                print("ID does not exist or no name was given")
        else:
            print("An ID and the name of what you're going to update the task to is needed to update a task")
    elif command == "delete":
        if len(wordsInUserInput) > 1:
            possibleID = wordsInUserInput[1]
            try:
                deletedTaskDescription = tasks[possibleID]["description"]
                del tasks[possibleID]
                with open("tasks.json", "w") as jsonfile:
                    json.dump(tasks, jsonfile, indent=4)
                print("Deleted " + "'" + deletedTaskDescription + "'")
            except:
                print("Index does not exist")
        else:
            print("An ID is needed to delete a task")
    elif command[:4] == "mark":
        if len(wordsInUserInput) > 1:
            possibleID = wordsInUserInput[1]
            try:
                tasks[possibleID]["status"] = command[5:]
                with open("tasks.json", "w") as jsonfile:
                    json.dump(tasks, jsonfile, indent=4)
            except:
                print("ID does not exist")
        else:
            print("An ID is needed to mark a task in progress, done, or another status")
    elif command == "list":
        if len(wordsInUserInput) > 1:
            possibleStatus = wordsInUserInput[1]
            for i in list(tasks.items()):
                if i[1]["status"] == possibleStatus:
                    printTaskInfo(i)
        else:
            for i in list(tasks.items()):
                printTaskInfo(i)