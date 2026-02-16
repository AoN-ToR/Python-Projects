import json
import time
import sys
import os

print("Welcome to the task manager. Please follow the instructions.")
time.sleep(3)

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
file = os.path.join(script_dir, "file.json")

def addTask(f_dict):
    taskName = input("Task title: ")
    if taskName in f_dict.keys():
        print("Name already used")
        return
    taskDescription = input("Task description: ")
    f_dict[taskName] = taskDescription
    print("Task has been added.")
    return f_dict

def delTask(f_dict):
    taskName = input("Task title: ")
    if taskName in f_dict.keys():
        f_dict.pop(taskName)
        print("Task has been removed.")
        return f_dict
    print("No such task is currently saved.")
    return f_dict


def loadFile(file):
    try:
        with open(file, 'r') as f:
            f_dict = json.load(f)
        return f_dict
    except FileNotFoundError:
        print("The file was not found. Creating a new one.")
        return {}
# at the end of the script, saves changes
def saveChanges(file, f_dict):
    try:
        with open(file, 'w') as f:
            f.write(json.dumps(f_dict))
        print("File Saved")
        return
    except FileNotFoundError:
        print("The file was not found. Cancelled writing data in json file")
        sys.exit(0)


f_dict = loadFile(file)
while True:
    user_input = input("\nChoose what to do next: \n(1) Add task\n(2) Delete task\n(3) See tasks\n(4) Quit\n")
    if user_input == "1" or user_input == "(1)":
        sys.stdout.write("\033[F")
        f_dict = addTask(f_dict)
        print("\r ")
    elif user_input == "2" or user_input == "(2)":
        sys.stdout.write("\033[F")
        print("\r ")
        f_dict = delTask(f_dict)
    elif user_input == "3" or user_input == "(3)":
        sys.stdout.write("\033[F")
        print("\r ")
        for k,v in f_dict.items():
            print(f"{k} : {v}")
    elif user_input == "4" or user_input == "(4)":
        sys.stdout.write("\033[F")
        print("\r ")
        break
    else:
        sys.stdout.write("\033[2K\r")
        sys.stdout.write("Given user input was not in the options. Please try again.")
        
try:
    saveChanges(file, f_dict)
except:
    print("Error while trying to save data.")