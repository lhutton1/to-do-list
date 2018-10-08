from flask import render_template
from app import app

"""
Index page
"""
@app.route('/')
def index():
    user = {'name' : 'Luke Hutton'}

    return render_template( 'index.html',
                            title='Simple template example',
                            user=user)
