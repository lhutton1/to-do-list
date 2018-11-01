import datetime
from app import db

"""
Model of a task. Holds all of the data needed to create an entry in the database
for a task. In this model ID is the primary key.
"""
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(500))
    completed = db.Column(db.Boolean)
    dateAdded = db.Column(db.DateTime)

    def __repr__(self):
        return '<Task {}>'.format(self.title)
