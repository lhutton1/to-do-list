from flask import request, render_template, redirect
from app import app, db
from app.models import Task
from app.forms import EditForm
import json
import datetime

"""
Index page

the argument filterBy can be used to filter the tasks:
    -   complete -> shows only tasks that are complete.
    -   incomplete -> shows only tasks that are incomplete.
    -   any other argument means all tasks are displayed.
"""
@app.route('/', methods=['GET'])
def index():
    title = 'To-do List'
    form = EditForm()
    taskOrderQuery = db.session.query(Task).order_by(Task.id.desc()).all()

    if request.method == 'GET':
        filter = request.args.get("filterBy", type = str)

        if filter == 'complete':
            taskOrderQuery = db.session.query(Task).filter_by(completed = True)
        if filter == 'incomplete':
            taskOrderQuery = db.session.query(Task).filter_by(completed = False)

    return render_template( 'index.html',
        title = title,
        tasks = taskOrderQuery,
        form = form
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
    newTask = Task(title='Not set', description='Not set', completed=False, dateAdded=datetime.datetime.now())
    db.session.add(newTask)
    db.session.commit()

    return json.dumps({'status': 'OK', 'response': 'new task', 'reload': True, 'newTaskId': newTask.id})

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
