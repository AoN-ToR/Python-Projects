import json
import time

print("Welcome to the task manager. Please follow the instructions.")
time.sleep(3)

file = "data.json"

def searchInFile(file, taskName):
    with open(file, "r") as f:
        if taskName in f:
            return True
        return False
    
def addToFile(file, taskName, taskDescription):
    with open(file, "a") as f:
        f.write(taskName + ":" + taskDescription)


def addTask():
    taskName = input("Task title: ")
    taskDescription = input("Task description: ")
    if searchInFile(file, taskName):
        print("Already there")
        return
    addToFile(file, taskName, taskDescription)
    return
def delTask():
    taskName = input("Task title: ")
    if searchInFile:
        delFromFile(file, taskName)
        return
    print("No such task in file.")
    return
        

while True:
    user_input = input("Choose what to do next: \n(1) Ajouter tâches\n(2) Supprimer tâches\n(3) Voir tâches\n(4) Quitter")
    