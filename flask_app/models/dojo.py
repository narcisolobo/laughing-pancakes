from pprint import pprint
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

DATABASE = 'dojos-ninjas'


class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    def __repr__(self):
        return f'<Dojo: {self.name}>'

    # create a dojo
    @classmethod
    def save(cls, data):
        query = 'INSERT INTO dojos (name) VALUES (%(name)s);'
        dojo_id = connectToMySQL(DATABASE).query_db(query, data)
        return dojo_id

    # find all dojos (no data needed)
    @classmethod
    def find_all(cls):
        query = 'SELECT * from dojos;'
        results = connectToMySQL(DATABASE).query_db(query)
        dojos = []
        for result in results:
            dojos.append(Dojo(result))
        return dojos

    # find one dojo by id
    @classmethod
    def find_by_id(cls, data):
        query = 'SELECT * from dojos WHERE id = %(id)s;'
        results = connectToMySQL(DATABASE).query_db(query, data)
        dojo = Dojo(results[0])
        return dojo

    # find one dojo by id with ninjas
    @classmethod
    def find_by_id_with_ninjas(cls, data):
        query = 'SELECT * from dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;'
        results = connectToMySQL(DATABASE).query_db(query, data)
        pprint(results)
        dojo = Dojo(results[0])

        """
        if we see the field 'dojo_id',
        we know that dojo has at least one ninja
        """

        if results[0]['dojo_id']:
            for result in results:
                ninja_data = {
                    'id': result['ninjas.id'],
                    'first_name': result['first_name'],
                    'last_name': result['last_name'],
                    'age': result['age'],
                    'created_at': result['created_at'],
                    'updated_at': result['updated_at'],
                    'dojo_id': result['dojo_id']
                }
                dojo.ninjas.append(ninja.Ninja(ninja_data))
        return dojo
