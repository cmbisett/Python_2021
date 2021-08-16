from flask import Flask

from flask_bcrypt import Bcrypt


app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = "sneaky sneaky safe thing" #create secret key for session


DB = "login_schema"  #create a global bariable for database being accessed by models/schema name
bcrypt = Bcrypt(app)