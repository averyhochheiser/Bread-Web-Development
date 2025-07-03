from . import db # importing db object
from flask_login import UserMixin
from sqlalchemy.sql import func # let SQL take care of date

# db model is layout for db object

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    # associtate different notes with different users
    # use foreign key - key on db table that ref id to another db column
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # ref user class and id field
    # one to many relationship - many notes for one user

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note') # relationship field is list of notes






