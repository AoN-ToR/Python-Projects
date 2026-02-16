def addTask(f_dict, taskName, taskDescription):
    if taskName in f_dict:
        return False, "Name already used"
    f_dict[taskName] = {"description": taskDescription, "done":False}
    return True, "Task added"

def delTask(f_dict, taskName):
    if taskName in f_dict:
        f_dict.pop(taskName)
        print("Task has been removed.")
        return True, "Task removed"
    return False, "Task not found"

def seeTask(f_dict):
    text = ""
    for k, v in f_dict.items():
        desc = v["description"]
        done = v["done"]
        text += f"{k}: {desc} " + ("(Done)\n" if done else "(Not done)\n")
    return True, text

def markDone(f_dict, taskName):
    if taskName in f_dict:    
        f_dict[taskName]["done"] = True
        return True, f"{taskName} marked done"
    else:
        return False, "Task not found"

def markUndone(f_dict, taskName):
    if taskName in f_dict:    
        f_dict[taskName]["done"] = False
        return True, f"{taskName} marked not done"
    else:
        return False, "Task not found"