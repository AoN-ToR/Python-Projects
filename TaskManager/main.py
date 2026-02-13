import json
import time

print("Welcome to the task manager. Please follow the instructions.")
time.sleep(3)

file = "file.json"

def addTask(f_dict):
    taskName = input("Task title: ")
    taskDescription = input("Task description: ")
    if taskName in f_dict.key():
        print("Already there")
        return
    f_dict[taskName] = taskDescription
    print("Task has been added.")
    return f_dict

def delTask(f_dict):
    taskName = input("Task title: ")
    if taskName in f_dict.key():
        f_dict.pop(taskName)
        print("Task has been removed.")
        return
    print("No such task is currently saved.")
    return f_dict


def loadFile(file):
    with open(file, 'r') as f:
        f_dict = json.loads(f)
    return f_dict
# at the end of the script, saves changes
def saveChanges(file, f_dict):
    with open(file, 'w') as f:
        f.write(json.dump(f_dict))
    print("File Saved")
    return


f_dict = loadFile("file.json")
while True:
    user_input = input("Choose what to do next: \n(1) Add task\n(2) Delete task\n(3) See tasks\n(4) Quit")
    if user_input == "1" | user_input == "(1)":
        f_dict = addTask(f_dict)
    elif user_input == "2" | user_input == "(2)":
        f_dict = delTask(f_dict)
    elif user_input == "3" | user_input == "(3)":
        for k,v in f_dict:
            print(f"{k} : {v}", k, v)
    elif user_input == "4" | user_input == "(4)":
        break
    else:
        print("Given user input was not in the options. Please try again.")

saveChanges(f_dict)