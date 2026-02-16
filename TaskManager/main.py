import os
import sys
import platform
from storage import loadFile, saveChanges
from tasks import addTask, delTask, seeTask, markDone, markUndone

FILE_PATH = "file.json"

print("Welcome to the task manager. Please follow the instructions.")

def pause_clear():
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


f_dict = loadFile(FILE_PATH)
while True:
    user_input = input("\nChoose what to do next: \n(1) Add task\n(2) Delete task\n(3) Mark task as done\n(4) Mark task as undone\n(5) See tasks\n(6) Quit\n")
    user_input = user_input.strip("() ")
    sys.stdout.write("\033[F")
    print("\r   ")
    if user_input == "1":
        taskName = input("Task title: ").strip()
        if not taskName:
            print("Task name cannot be empty")
            continue
        taskDescription = input("Task description: ").strip()
        success, msg = addTask(f_dict, taskName, taskDescription)
        print(msg)
        pause_clear()
    elif user_input == "2":
        taskName = input("Task title: ").strip()
        if not taskName:
            print("Task name cannot be empty")
            continue
        success, msg = delTask(f_dict, taskName)
        print(msg)
        pause_clear()
    elif user_input == "3":
        taskName = input("Task title: ").strip()
        if not taskName:
            print("Task name cannot be empty")
            continue
        success, msg = markDone(f_dict, taskName)
        print(msg)
        pause_clear()
    elif user_input == "4":
        taskName = input("Task title: ").strip()
        if not taskName:
            print("Task name cannot be empty")
            continue
        success, msg = markUndone(f_dict, taskName)
        print(msg)
        pause_clear()
    elif user_input == "5":
        succes, msg = seeTask(f_dict)
        print(msg)
        pause_clear()
    elif user_input == "6":
        break
    else:
        sys.stdout.write("\033[F")
        sys.stdout.write("\rGiven user input was not in the options. Please try again.\n")
        pause_clear()
        
try:
    saveChanges(FILE_PATH, f_dict)
except Exception as e:
    print("Error while trying to save data:", e)