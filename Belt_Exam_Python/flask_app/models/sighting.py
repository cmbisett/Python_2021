#import the mysqlconnection, establishes connection to the database
from flask_app.config.mysqlconnection import connectToMySQL
import re                               #re is used for regular expressions in python
from flask import flash                 #Flash to display error messages from validation
from flask_app import app, DB, bcrypt   #import app, the databse, bcrypt

#connect the other model into the file, but do not call it by its class, call the file name, then call the class using the file name
from flask_app.models import user


class Sighting:
    #Setup the constructor, with all attributes that match the users table fields. 
    def __init__(self, data):
        self.id = data['id']
        #establishing absraction and a one to many relationship
        if data['user_id']:                                        #prevent an infinite loop if the user_id is in the database
            self.user = user.User.get_one({"id": data['user_id']}) # this the relationship of the tables through the foreign key
        self.location = data['location']
        self.date = data['date']
        self.info = data['info']
        self.number = data['number']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls, data): #create a row of data in the database 
        query = """
            INSERT INTO sightings (user_id, location, date, info, number)
            VALUES (%(user_id)s, %(location)s, %(date)s, %(info)s, %(number)s);
        """

        #set the result equal to the database function, pass the database name, query, and data to create new row
        result = connectToMySQL(DB).query_db(query, data)
        return result


    @classmethod
    def get_all(cls): #get all the data from entire table
        query = "SELECT * FROM sightings"
        results = connectToMySQL(DB).query_db(query)
        print(results) #result is always a list of  dictionary

        #create list to store the all the rows from the database
        all_sightings = [] 

        for row in results:
            all_sightings.append(cls(row)) #append to a list of objects

        return all_sightings   


    #every function except for get_all() requires a dictionary to be passed into its parameter for data
    @classmethod
    def get_one(cls, data):
        #We must pass a dictionary into the query_db(query, data)
        query = "SELECT * FROM sightings WHERE id = %(id)s;"
        result = connectToMySQL(DB).query_db(query, data)

        #if the selection does not exist, return false 
        if len(result) < 1:
            return False
        else:
            return cls(result[0])


    @classmethod
    def update(cls, data): #edit the the data within a row of the table within database
        query = "UPDATE sightings SET location = %(location)s, date = %(date)s, info = %(info)s, number = %(number)s WHERE id = %(id)s;"

        return connectToMySQL(DB).query_db(query, data)

        
    @classmethod
    def delete(cls, data): #delete from a specific row, set the id
        query = "DELETE FROM sightings WHERE id = %(id)s;"

        return connectToMySQL(DB).query_db(query, data)
        

    @staticmethod
    def validate_sighting(form_data): #validation is the process of sanitizing the input from the user taken from the form
        is_valid = True 
        
        if len(form_data['location']) < 2:
            flash("location field required", "location")
            is_valid = False

        if len(form_data['date']) != 10:
            flash("Please make sure date is inputted correctly", "date")
            is_valid = False

        if len(form_data['info']) < 2:
            flash("info field required", "info")
            is_valid = False

        if int(form_data['number']) < 1:
            flash("number of sasquatches must be at least one", "number")
            is_valid = False


        return is_valid    
    