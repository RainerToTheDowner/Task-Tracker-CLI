import json
import os

tasks = {}

if os.path.exists("tasks.json") == False:
    with open("tasks.json", "w") as jsonfile:
        json.dump(tasks, jsonfile, indent=4)
else:
    with open("tasks.json", "r") as jsonfile:
        tasks = json.load(jsonfile)