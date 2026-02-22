from database import addTask as dbAdd, delTask as dbDel, markDone as dbDone, markUndone as dbUndone, getTasks as dbGetTasks

def addTask(name, description):
    return dbAdd(name, description)

def delTask(name):
    return dbDel(name)

def markDone(name):
    return dbDone(name)

def markUndone(name):
    return dbUndone(name)

def getTasks():
    return dbGetTasks()