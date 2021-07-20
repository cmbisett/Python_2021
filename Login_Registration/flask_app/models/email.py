from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re




class Email:
    def __init__(self, data):
        self.id = data["id"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]


    # this is creating a new ninja
    @classmethod
    def create(cls, data):
        # data is a dictionary containing all the data from the form
        query = """
            INSERT INTO emails (email)
            VALUES (%(email)s);
        """
        email_id = connectToMySQL("email_schema").query_db(query, data)

        return email_id


    # this is getting all emails
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM emails;"
        results = connectToMySQL("email_schema").query_db(query)
        # results is always a list of dictionaries

        return [cls(row) for row in results]


    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM emails WHERE email = %(email)s"
        results = connectToMySQL("email_schema").query_db(query, data)
        
        if len(results) >=1:
            return cls(results[0])
        else: return results

        return email


    @staticmethod
    def validate(form):
        is_valid = True
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        if not EMAIL_REGEX.match(form['email']): 
            flash("Invalid email format!")
            is_valid = False
        
        elif not Email.get_one({"email": form['email']}) == False:
            flash("Email already exists")
            is_valid  = False

        return is_valid