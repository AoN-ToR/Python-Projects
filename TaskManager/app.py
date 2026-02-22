from flask import Flask, render_template, request, redirect, url_for, flash
from tasks import addTask, markDone, markUndone, delTask
from storage import loadFile, saveChanges

FILE_PATH = "file.json"

app = Flask(__name__)
app.secret_key="secret"

@app.route('/')
def homepage():
    tasks = loadFile(FILE_PATH)
    return render_template('homepage.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    taskName=request.form.get("taskName", "").strip()
    taskName = taskName.replace(" ", "_")
    taskDesc=request.form.get("description", "").strip()
    
    tasks=loadFile(FILE_PATH)
    addTask(tasks, taskName, taskDesc)
    saveChanges(FILE_PATH, tasks)
    
    flash("Task added")
    
    return redirect('/')

@app.route('/delete/<taskName>')
def delete(taskName):
    tasks=loadFile(FILE_PATH)
    delTask(tasks, taskName)
    saveChanges(FILE_PATH, tasks)
    
    flash("Task deleted")
    
    return redirect('/')

@app.route('/done/<taskName>')
def done(taskName):
    tasks=loadFile(FILE_PATH)
    markDone(tasks, taskName)
    saveChanges(FILE_PATH, tasks)
    
    return redirect('/')

@app.route('/undone/<taskName>')
def undone(taskName):
    tasks=loadFile(FILE_PATH)
    markUndone(tasks, taskName)
    saveChanges(FILE_PATH, tasks)
    
    return redirect('/')

@app.route('/stats')
def stats():
    tasks=loadFile(FILE_PATH)
    nb_task=len(tasks.keys())
    nb_done=0
    for task in tasks.values():
        if task['done']:
            nb_done += 1
    if nb_task == 0:
        completion = 0
    else:
        completion = round(nb_done / nb_task * 100)
    return render_template('stats.html', nb_task=nb_task, nb_done=nb_done, completion=completion)

if __name__ == "__main__":
    app.run(debug=True)