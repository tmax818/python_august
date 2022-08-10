# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
# model the class after the user table from our database

DATABASE = "users"

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database


    ## ! CREATE
    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);"
        ## prepared statement varibles must match keys in data dict
        return connectToMySQL(DATABASE).query_db(query, data)


    ## ! READ/RETRIEVE ALL
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(DATABASE).query_db(query)
        users = []
        for user in results:
            users.append( User(user) )
        return users

    ## ! READ/RETRIEVE ONE 
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id=%(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        user = User(result[0])
        return user

