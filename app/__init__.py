from flask import Flask, render_template, request
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Resource, Api
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# jinja 2 extensions
app.jinja_env.add_extension('jinja2.ext.do')

# flask add ons
Scss(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app)

from app import views
from app import models
