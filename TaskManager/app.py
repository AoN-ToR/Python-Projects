from flask import Flask, render_template, request, redirect, flash
from tasks import addTask, delTask, markDone, markUndone, getTasks
from database import init_db

# Init DB
init_db()

app = Flask(__name__)
app.secret_key = "my_secret_key"

# Routes

@app.route('/')
def homepage():
    tasks = getTasks()
    return render_template('homepage.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    taskName = request.form.get("taskName", "").strip().replace(" ", "_")
    taskDesc = request.form.get("description", "").strip()
    
    msg = addTask(taskName, taskDesc)
    flash(msg)
    return redirect('/')

@app.route('/delete/<taskName>')
def delete(taskName):
    msg = delTask(taskName)
    flash(msg)
    return redirect('/')

@app.route('/done/<taskName>')
def done(taskName):
    msg = markDone(taskName)
    flash(msg)
    return redirect('/')

@app.route('/undone/<taskName>')
def undone(taskName):
    msg = markUndone(taskName)
    flash(msg)
    return redirect('/')

@app.route('/stats')
def stats():
    tasks = getTasks()
    nb_task = len(tasks)
    nb_done = sum(1 for t in tasks.values() if t["done"])
    completion = round(nb_done / nb_task * 100) if nb_task else 0
    return render_template('stats.html', nb_task=nb_task, nb_done=nb_done, completion=completion)

# Run app
if __name__ == "__main__":
    app.run(debug=True)