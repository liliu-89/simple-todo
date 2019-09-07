import os
from sqla_wrapper import SQLAlchemy

db = SQLAlchemy(os.getenv("DATABASE_URL", "sqlite:///localhost.sqlite")) # this connects to a database either on Heroku or on localhost

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    todo = db.Column(db.String)
    check = db.Column(db.Boolean)
