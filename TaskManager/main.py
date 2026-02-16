import json
import time
import sys
import os
import platform

print("Welcome to the task manager. Please follow the instructions.")
time.sleep(3)

def next():
    input("\n\nPress Enter to keep going.")
    try:
        # Detect operating system
        current_os = platform.system()
        
        if current_os == "Windows":
            os.system('cls')  # Windows
        else:
            os.system('clear')  # macOS/Linux
    except Exception as e:
        print(f"Error clearing terminal: {e}")


# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
file = os.path.join(script_dir, "file.json")

def addTask(f_dict):
    taskName = input("Task title: ")
    if taskName in f_dict.keys():
        print("Name already used")
        return
    taskDescription = input("Task description: ")
    f_dict[taskName] = {"description": taskDescription, "done":False}
    print("Task has been added.")
    return

def delTask(f_dict):
    taskName = input("Task title: ")
    if taskName in f_dict.keys():
        f_dict.pop(taskName)
        print("Task has been removed.")
        return
    print("No such task is currently saved.")
    return

def seeTask(f_dict):
    for k, v in f_dict.items():
        desc = v["description"]
        done = v["done"]
        print(f"{k}: {desc} "+("(Done)" if done else "(Not done)"))

def markDone(f_dict):
    taskName = input("Enter Task Name: ")
    if taskName in f_dict.keys():    
        f_dict[taskName]["done"] = True
        print(f"{taskName} is now marked as done !")
    else:
        print("Task not registered")
def markUndone(f_dic):
    taskName = input("Enter Task Name: ")
    if taskName in f_dict.keys():    
        f_dict[taskName]["done"] = False
        print(f"{taskName} is now marked as undone !")
    else:
        print("Task not registered")

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
            json.dump(f_dict, f, indent=4)
        print("File Saved")
        return
    except FileNotFoundError:
        print("The file was not found. Cancelled writing data in json file")
        sys.exit(0)


f_dict = loadFile(file)
while True:
    user_input = input("\nChoose what to do next: \n(1) Add task\n(2) Delete task\n(3) Mark task as done\n(4) Mark task as undone\n(5) See tasks\n(6) Quit\n")
    user_input = user_input.strip("() ")
    if user_input == "1":
        sys.stdout.write("\033[F")
        print("\r   ")
        addTask(f_dict)
        next()
    elif user_input == "2":
        sys.stdout.write("\033[F")
        print("\r   ")
        delTask(f_dict)
        next()
    elif user_input == "3":
        sys.stdout.write("\033[F")
        print("\r   ")
        markDone(f_dict)
        next()
    elif user_input == "4":
        sys.stdout.write("\033[F")
        print("\r   ")
        markUndone(f_dict)
        next()
    elif user_input == "5":
        sys.stdout.write("\033[F")
        print("\r   ")
        seeTask(f_dict)
        next()
    elif user_input == "6":
        sys.stdout.write("\033[F")
        print("\r   ")
        break
    else:
        sys.stdout.write("\033[F")
        sys.stdout.write("\rGiven user input was not in the options. Please try again.\n")
        next()
        
try:
    saveChanges(file, f_dict)
except Exception as e:
    print("Error while trying to save data:", e)