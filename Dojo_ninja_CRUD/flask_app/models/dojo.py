from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models import ninja

class Dojo:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.ninjas = []

    @classmethod
    def create(cls, data):
        # data is a dictionary containing all the data from the form
        query = """
            INSERT INTO dojos (name)
            VALUES (%(name)s);
        """
        dojo_id = connectToMySQL("dojos_ninjas").query_db(query, data)
        
        return dojo_id

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL("dojos_ninjas").query_db(query)
        # results is always a list of dictionaries

        return [cls(row) for row in results]
        

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM dojos JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s"
        results = connectToMySQL("dojos_ninjas").query_db(query, data)

        dojo = cls(results[0])

        for row in results:
            row_data = {
                "id": row["ninjas.id"],
                "first_name": row["first_name"],
                "last_name": row["last_name"],
                "age": row["age"],
                "created_at": row["created_at"],
                "updated_at": row["updated_at"]
            }

            dojo.ninjas.append(ninja.Ninja(row_data))

        return dojo