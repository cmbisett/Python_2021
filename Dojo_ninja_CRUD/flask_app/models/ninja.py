from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models import dojo

class Ninja:
    def __init__(self, data):
        self.id = data["id"]
        if "dojo_id" in data:
            self.dojo = dojo.Dojo.get_one({"id": data['dojo_id']})
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age = data["age"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]


    # this is creating a new ninja
    @classmethod
    def create(cls, data):
        # data is a dictionary containing all the data from the form
        query = """
            INSERT INTO ninjas (dojo_id, first_name, last_name, age)
            VALUES (%(dojo_id)s, %(first_name)s, %(last_name)s, %(age)s);
        """
        ninja_id = connectToMySQL("dojos_ninjas").query_db(query, data)

        return ninja_id


    # this is getting all ninjas
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL("dojos_ninjas").query_db(query)
        # results is always a list of dictionaries

        return [cls(row) for row in results]