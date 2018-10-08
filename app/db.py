from app import app
from flask import g
import sqlite3

DATABASE = '../assets/database.db'

"""
Connect database
"""
def get_db():
    db = getattr(g, '_database', None)

    if db is None:
        db = g._database = sqlite3.connect(DATABASE)

    return db


"""
Close databse connection
"""
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)

    if db is not None:
        db.close()
