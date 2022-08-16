from email.policy import default
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    img = db.Column(db.Text)
    name = db.Column(db.Text)
    mimetype = db.Column(db.Text)
    clothing_id = db.Column(db.Integer, db.ForeignKey('clothing.id'))


class Clothing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    color = db.Column(db.String(100))
    type = db.Column(db.String(100))
    storage = db.Column(db.String(100))
    size = db.Column(db.String(5))
    last_worn = db.Column(db.DateTime(timezone=True), default=None)
    clean = db.Column(db.Boolean, default=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    images = db.relationship('Image')


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    clothing = db.relationship('Clothing')
