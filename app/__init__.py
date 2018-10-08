from flask import Flask, render_template
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

app = Flask(__name__)
app.config['TESTING'] = True
app.config.from_object(Config)

Scss(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import views
from app import models
