from flask import Flask, render_template, request, redirect
from tasks import addTask, markDone, markUndone, delTask
from storage import loadFile, saveChanges

FILE_PATH = "file.json"

app = Flask(__name__)

@app.route('/')
def homepage():
    tasks = loadFile(FILE_PATH)
    return render_template('homepage.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    taskName=request.form.get("taskName", "").strip()
    taskDesc=request.form.get("description", "").strip()
    
    tasks=loadFile(FILE_PATH)
    addTask(tasks, taskName, taskDesc)
    saveChanges(FILE_PATH, tasks)
    
    return redirect('/')

@app.route('/delete/<taskName>')
def delete(taskName):
    tasks=loadFile(FILE_PATH)
    delTask(tasks, taskName)
    saveChanges(FILE_PATH, tasks)
    
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

if __name__ == "__main__":
    app.run(debug=True)