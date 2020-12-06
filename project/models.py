from flask_login import UserMixin
from . import db

# making table users
class Users(db.Model, UserMixin):
    __tablename__ = 'users'
    id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(100),unique=True)
    password=db.Column(db.String(100))
    name=db.Column(db.String(1000))

# making table testnames
class TestNames(db.Model):
    __tablename__='testnames'
    id=db.Column(db.Integer,primary_key=True)
    testnames=db.Column(db.String(100))

# making table usertestscore
class TestScore(db.Model):
    __tablename__ = 'usertestscore'
    id=db.Column(db.Integer,primary_key=True)
    date=db.Column(db.DateTime())
    user_id=db.Column(db.Integer, db.ForeignKey('users.id'))
    testnames_id=db.Column(db.Integer, db.ForeignKey('testnames.id'))
