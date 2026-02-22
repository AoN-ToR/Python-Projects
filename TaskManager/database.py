import sqlite3

DB_PATH = "tasks.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

def init_db():
    co = get_connection()
    cursor = co.cursor()
    
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS tasks (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name TEXT UNIQUE NOT NULL,
                       description TEXT,
                       done INTEGER NOT NULL)
                   """)
    co.commit()
    co.close()
    
def getTasks():
    co = get_connection()
    cursor = co.cursor()
    
    cursor.execute("""
                   SELECT id, name, description, done FROM tasks
                   """)
    rows = cursor.fetchall()
    co.close()
    
    tasks = {}
    for row in rows:
        tasks[row[1]] = {"id": row[0], "description": row[2], "done": bool(row[3])}
        
    return tasks

def markDone(name):
    co = get_connection()
    cursor = co.cursor()
    cursor.execute("""
                   UPDATE tasks SET done = 1 WHERE name = ?
                   """, (name,))
    co.commit()
    co.close()
    
def markUndone(name):
    co = get_connection()
    cursor = co.cursor()
    cursor.execute("""
                   UPDATE tasks SET done = 0 WHERE name = ?
                   """, (name,))
    co.commit()
    co.close()
    
def addTask(name, description):
    co = get_connection()
    cursor = co.cursor()
    try:
        cursor.execute("""
                       INSERT INTO tasks (name, description, done) VALUES (?, ?, 0)
                       """, (name, description))
        co.commit()
    except sqlite3.IntegrityError:
        print(f"Tâche '{name}' existe déjà !")
    finally:
        co.close()
        
def delTask(name):
    co = get_connection()
    cursor = co.cursor()
    cursor.execute("""
                   DELETE FROM tasks WHERE name = ?
                   """, (name,))
    co.commit()
    co.close()