from . import  db
from flask_login import UserMixin
from sqlalchemy.sql import func
from werkzeug.security import generate_password_hash, check_password_hash

# User model: stores info about each person who signs up.
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)  # User's ID number
    email = db.Column(db.String(150), unique=True)  # User's email (must be different for each user)
    password = db.Column(db.String(150), nullable=False)  # User's password (saved safely)
    username = db.Column(db.String(150))  # User's name
    notes = db.relationship('Note')  # All notes this user has made

    def set_password(self, password):
        # Saves the password in a safe way
        self.password = generate_password_hash(password)

    def check_password(self, password):
        # Checks if the password is correct
        return check_password_hash(self.password, password)

# Note model: stores each note a user writes.
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Note's ID number
    data = db.Column(db.String(10000))  # What the note says
    date = db.Column(db.DateTime(timezone=True), default=func.now())  # When the note was made
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # Which user made the note