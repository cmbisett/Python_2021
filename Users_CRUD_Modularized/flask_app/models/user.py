from flask_app.config.myslqconnection import connectToMySQL

class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

# CREATES A NEW USER
    @classmethod
    def create(cls, data):
        query = """
            INSERT INTO users(first_name,last_name,email)
            VALUES (%(first_name)s, %(last_name)s, %(email)s);
        """

        user_id = connectToMySQL('users').query_db(query,data)
        return user_id

# DISPLAYS ALL USERS
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('users').query_db(query)  #dont need data becuase its a whole table, not a specific col

        all_users = []

        for row in results:
            # row is each individual dictionary in the results list
            # cls(row) is instantiaing a Dog object 
            # appending to a our list of dog objects
            all_users.append(cls(row))
        
        return all_users

# DISPLAYS ONE USER BY ID
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL("users").query_db(query, data)

        # results is a list of dictionaries
        # results[0] is the dict at index of 0

        return cls(results[0])

# UPDATES ONE USER BY ID
    @classmethod
    def update(cls, data):
        # print(data)
        query = """
                UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s,
                email = %(email)s, updated_at = NOW() 
                WHERE id = %(id)s;
            """
        updated = connectToMySQL("users").query_db(query, data)

        return updated

# DELETES A USER BY ID
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s"

        delete = connectToMySQL("users").query_db(query, data)
        return delete