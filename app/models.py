import datetime
from app import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(500))
    completed = db.Column(db.Boolean)
    dateAdded = db.Column(db.DateTime)

    def __repr__(self):
        return '<Task {}>'.format(self.title)