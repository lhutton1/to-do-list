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
@app.route('/index', methods=['GET'])
def index():
    title = 'To-do List'
    taskOrderQuery = db.session.query(Task).order_by(Task.id.desc()).all()

    if request.method == 'GET':
        filter = request.args.get("filterBy", type = str)

        if filter == 'complete':
            taskOrderQuery = db.session.query(Task).filter_by(completed = True)
        if filter == 'incomplete':
            taskOrderQuery = db.session.query(Task).filter_by(completed = False)

    return render_template( 'index.html',
        title = title,
        tasks = taskOrderQuery
    )

"""
Add new task page

Provides a form to create a new task.
"""
@app.route('/addNewTask', methods=['GET', 'POST'])
def addNewTask():
    form = EditForm()

    if form.validate_on_submit():
        newTask = Task(title=form.title.data, description=form.description.data, completed=False, dateAdded=datetime.datetime.now())
        db.session.add(newTask)
        db.session.commit()

        return redirect('/')

    return render_template('new-task.html', title='Add New Task', form=form)


"""
Remove a task
"""
@app.route('/removeTask', methods=['GET'])
def removeTask():
    if request.method == 'GET':
        taskID = request.args.get("taskId", type = int)

        db.session.delete(Task.query.get(taskID))
        db.session.commit()

    return redirect('/')


"""
Mask task as complete or incomplete
"""
@app.route('/markTask', methods=['GET'])
def markTask():
    if request.method == 'GET':
        taskID = request.args.get("taskId", type = str)
        complete = request.args.get("complete", type = str)

        try:
            taskID = int(taskID)
        except:
            return redirect('/')

        if complete == "True":
            try:
                task = Task.query.get(taskID)
                task.completed = True
            except:
                return redirect('/')
        elif complete == "False":
            try:
                task = Task.query.get(taskID)
                task.completed = False
            except:
                return redirect('/')

        db.session.commit()

    return redirect('/')
