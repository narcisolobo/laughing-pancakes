from pprint import pprint
from flask_app.config.mysqlconnection import connectToMySQL

DATABASE = 'dojos-ninjas'


class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    def __repr__(self):
        return f'<Ninja: {self.first_name} {self.last_name}>'


    # create a ninja
    @classmethod
    def save(cls, data):
        query = 'INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);'
        ninja_id = connectToMySQL(DATABASE).query_db(query, data)
        return ninja_id
