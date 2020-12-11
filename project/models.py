from flask_login import UserMixin
from . import db

# making table users
class Users(db.Model, UserMixin):
    __tablename__ = 'users'
    id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(100),unique=True)
    password=db.Column(db.String(100))
    name=db.Column(db.String(1000))
