from flask import Flask, render_template
from flask_scss import Scss

app = Flask(__name__)
app.config['TESTING'] = True

Scss(app)

from app import views
