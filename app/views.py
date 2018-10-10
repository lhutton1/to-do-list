from flask import request, render_template
from app import app, db
from app.models import Task
import json

"""
Index page
"""
@app.route('/')
def index():
    user = {'name' : 'luke hutton'}

    return render_template( 'index.html',
        title='To-do list',
        user=user,
        tasks=db.session.query(Task).all(),
        isEdit=False
    )

"""
respond to AJAX request
"""
@app.route('/respond', methods=['POST'])
def respond():
    # parse JSON
    data = json.loads(request.data)
    task_id = data.get('id')
    task_parent_id = int(data.get('parentId').split('-')[1])
    #task = Task.query.get()

    # detect which action has been pressed and perform relevent database action.
    if (data.get('id') == "delete"):
        db.session.delete(Task.query.get(task_parent_id))
        db.session.commit()

    # return request
    return json.dumps({'status': 'OK', 'response': task_parent_id})
