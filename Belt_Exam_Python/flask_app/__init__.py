from flask import Flask
from flask_bcrypt import Bcrypt   

app = Flask(__name__)    
bcrypt = Bcrypt(app) 

DB = "belt_schema" 
app.secret_key = "dont ask if dont know" 

