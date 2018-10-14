from flask import request, render_template, redirect
from app import app, db, databaseView
from app.models import Task
import json

"""
Index page
"""
@app.route('/')
def index():
    taskView = 0
    if databaseView == 0:
        taskView = db.session.query(Task).order_by(Task.id.desc()).all()
    elif databaseView == 1:
        taskView = db.session.query(Task).order_by(Task.id.desc()).filter_by(completed = True)
    elif databaseView == 2:
        taskView = db.session.query(Task).order_by(Task.id.desc()).filter_by(completed = False)

    return render_template( 'index.html',
        title='To-do list',
        tasks=db.session.query(Task).order_by(Task.id.desc()).all()
    )

"""
AJAX request to load tasks
"""
@app.route('/deleteTask', methods=['POST'])
def deleteTask():
    # parse JSON
    data = json.loads(request.data)
    task_parent_id = int(data.get('parentId').split('-')[1])

    # detect which action has been pressed and perform relevent database action.
    try:
        db.session.delete(Task.query.get(task_parent_id))
        db.session.commit()
        return json.dumps({'status': 'OK', 'response': 'task deleted', 'reload': True})
    except:
        return json.dumps({'status': 'ERROR', 'response': 'task could not be deleted'})

"""
AJAX request to edit task in the database
"""
@app.route('/editTask', methods=['POST'])
def editTask():
    data = json.loads(request.data)
    task_parent_id = int(data.get('parentId').split('-')[1])
    title = data.get('title')
    description = data.get('description')

    try:
        task = Task.query.get(task_parent_id)
        task.title = title
        task.description = description
        db.session.commit()
        return json.dumps({'status': 'OK', 'response': 'task edited', 'reload': True, 'data': [title, description]})
    except:
        return json.dumps({'status': 'ERROR', 'response': 'task could not be edited'})

"""
AJAX request to add task to the database
"""
@app.route('/newTask', methods=['POST'])
def newTask():
    newTask = Task(title='Not set', description='Not set', completed=False)
    db.session.add(newTask)
    db.session.commit()

    return json.dumps({'status': 'OK', 'response': 'new task', 'reload': True, 'newTaskId': newTask.id})
    #return json.dumps({'status': 'ERROR', 'response': 'task could not be edited'})

"""
AJAX request to change completed state of a task
"""
@app.route('/changeComplete', methods=['POST'])
def changeComplete():
    data = json.loads(request.data)
    task_parent_id = int(data.get('parentId').split('-')[1])
    completed = data.get('completed')

    try:
        task = Task.query.get(task_parent_id)
        task.completed = completed
        db.session.commit()
        return json.dumps({'status': 'OK', 'response': 'change complete', 'completed': completed, 'reload': True})
    except:
        return json.dumps({'status': 'ERROR', 'response': 'task could not be edited'})

"""
AJAX request to change task order
"""
@app.route('/changeTaskOrder', methods=['POST'])
def changeTaskOrder():
    databaseView = 2
    return json.dumps({'status': 'OK', 'response': 'new task', 'reload': True})
