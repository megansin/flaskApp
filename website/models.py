from email.policy import default
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

# class Storage(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100))
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     clothing = db.relationship('Clothing')


class Clothing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    color = db.Column(db.String(100))
    type = db.Column(db.String(100))
    storage = db.Column(db.String(100))
    seasons = db.Column(db.String(100))
    size = db.Column(db.String(5))
    last_worn = db.Column(db.DateTime(timezone=True), default=None)
    clean = db.Column(db.Boolean, default=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

#   seasons VARCHAR(40) NOT NULL,
#   last_worn DATE,
#   pic_file_name VARCHAR(200),


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    clothing = db.relationship('Clothing')
