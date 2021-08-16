#omport the mysqlconnection, establishes connection to the data base
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import app, bcrypt, DB #Db is where the schemas are located
import re

class User:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]


    @classmethod
    def create(cls, data):
        # data is a dictionary containing all the data from the form
        query = """
            INSERT INTO users (first_name, last_name, email, password)
            VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);
        """
        user_id = connectToMySQL(DB).query_db(query, data)

        return user_id


    # this is getting all emails
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(DB).query_db(query)
        # results is always a list of dictionaries

        return [cls(row) for row in results]


    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(DB).query_db(query, data)
    
        return cls(results[0])

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(DB).query_db(query, data)

        if len(results) < 1:
            return False
        
        return cls(results[0])


    @staticmethod
    def validate_user(form):
        is_valid = True
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        #Email validation =================================
        if not EMAIL_REGEX.match(form['email']): 
            flash("Invalid email format!")
            is_valid = False
        
        elif User.get_by_email({"email": form['email']}):
            flash("Email already exists")
            is_valid  = False

        #First Name validation ==================================
        if len(form['first_name']) <2:
            flash('First name must be at least 2 charcters')
            is_valid = False

        #Last Name validation ===============================
        if len(form['last_name']) <2:
            flash('Last name must be at least 2 charcters')
            is_valid = False

        #Password validation ============================
        if len(form['password']) < 8:
            flash('Password name must be at least 8 charcters')
            is_valid = False
        elif form['password'] != form['confirm_password']:
            flash('Password and Confrim Password must match!')
            is_valid = False

        return is_valid


    @staticmethod
    def login_validate(form):
        user = User.get_by_email({"email": form['email']})

        if not user:
            flash("Invalid Credentials")
            return False
        
        if not bcrypt.check_password_hash(user.password, form['password']):
            flash("Invalid Credentials")
            return False
        
        return True