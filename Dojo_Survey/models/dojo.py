from config.mysqlconnection import connectToMySQL
from flask import flash


class Dojo:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.location = data["location"]
        self.language = data["language"]
        self.comment = data["comment"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]


    @classmethod
    def create(cls, data):
        # data is a dictionary containing all the data from the form
        query = """
            INSERT INTO dojos (name, location, language, comment)
            VALUES (%(name)s, %(location)s, %(language)s, %(comment)s);
        """
        dojo_id = connectToMySQL("dojo_survey").query_db(query, data)
        
        return dojo_id
        

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM dojos WHERE dojos.id = %(id)s"
        results = connectToMySQL("dojo_survey").query_db(query, data)

        dojo = cls(results[0])

        return dojo



    @staticmethod
    def validate(form):
        is_valid = True

        if len(form['name']) < 3:
            flash("Name needs to be more than 3 characters.")
            is_valid = False
        elif form['name'].isnumeric():
            flash("Name needs to be more than 3 characters.")
            is_valid = False

        if len(form['location']) < 2:
            flash("Location needs to be more than 5 characters.")
            is_valid = False
        elif form['location'].isnumeric():
            flash("Location needs to be more than 5 characters.")
            is_valid = False

        if len(form['language']) < 1:
            flash("Language needs to be more than 1 characters.")
            is_valid = False

        return is_valid