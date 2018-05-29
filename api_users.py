from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask_jsonpify import jsonify

mysql = create_engine('mysql://cluck.users.db')
app = Flask(_name_)
api = Api(app)

class users(Resource):
    def get(self):
        conn = mysql.connect()  # подключаемся к базе данных
        query = conn.execute ('select * from username')  # Выполняем запрос и возвращаем результат json
        result = {'users':[i[1] for i in query.cursor.fetchall()]} # выбираем второй столбец, который является именем пользователя
        return jsonify(result)
    def post(self):
        conn = mysql.connect()  # подключаемся к базе данных
        print(request.json)
        id = request.json['id']
        username = request.json['username']
        name = request.json['name']
        surname = request.json['surname']
        password_hash = request.json['password_hash']
        access_token = request.json['access_token']
        auth_key = request.json['auth_key']
        created_at = request.json['created_at ']
        query = conn.execute("Insert into values(null,'{0}','{1}','{2}','{3}','{4}','{5}','{6}')".format(id,username, name, surname,
                                                                                                         password_hash, access_token, auth_key, created_at))
        return {'status': 'success'}


class users_id(Resource):
    def get(self):
        conn = mysql.connect()  # подключаемся к базе данных
        query = conn.execute('select * from id')  # Выполняем запрос и возвращаем результат json
        result = {'users_id': [i[0] for i in query.cursor.fetchall()]}  # выбираем первый  столбец, который является индификатором пользователя
        return jsonify(result)

api.add_resourse(users, '/users')
api.add_resourse(users_id, '/users/<:id>')



if __name__ == '__main__':
    app.run(port='5002')

