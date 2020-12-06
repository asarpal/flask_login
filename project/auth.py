from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from .models import Users
from flask_login import login_user
from . import db

auth=Blueprint('auth',__name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/loginpost', methods=[ 'POST'])
def loginpost():
    # fetch the values from the html form
    em=request.form.get('email')
    password=request.form.get('password')
    remember=True if request.form.get('remember') else False
    #check if email of user exists
    user=Users.query.filter_by(email=em).first()

    #cheks if the user exists
    #turns the password into hashed password and checks if the password is correct
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login')) # if the user doesn't exist or password is wrong reload the page

    #if everything entered is correct then the user gets logged in
    login_user(user, remember=remember)
    return redirect(url_for('main.profile'))

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signuppost', methods=['POST'])
def signuppost():
    # fetch the values from the html form

    em=request.form.get('email')
    name=request.form.get('name')
    password= request.form.get('password')

    # check if the user already exists in the database
    user=Users.query.filter_by(email=em).first()

    if user:
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))
    # truns the users password to a hashed password to make it secure
    new_user=Users(email=em, name=name, password=generate_password_hash(password,method='sha256'))
    # adding new user
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))

@auth.route('/logout')
def logout():
    return 'Logout'
