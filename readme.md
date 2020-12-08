# Flask_login
## Flask Start up
  - In terminal run the command below to start and set up flask.
    `export FLASK_APP=project`
    then
    `flask run`
## Creating DB
  - In terminal run below command to create DB.
    `>>> from project import db, create_app`
    `>>> db.create_all(app=create_app())`
## Making Signup function
### Check if database already has the email id entered  
  - In auth.py use the code below to check if email already exists.
    `user = Users.query.filter_by(email=email).first()`
### Hashing passwords
    Hashing passwords make the password secure that no one can hack it.
  - To hash passwords use the code below.
    `new_user=Users(email=em, name=name, password=generate_password_hash(password, method='sha256'))`
  - To check the hashed password with the normal password use the code below.
    `if not user or not check_password_hash(user.password, password):`
       `return redirect(url_for('auth.login'))`
     `else:`
         `redirect(url_for('main.profile'))`
