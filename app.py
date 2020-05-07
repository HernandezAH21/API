from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

users = [
    {
        "name": "Alan",
        "email": "serrato.alan21@gmail.com",
        "password": "Guatemalasur1719"
    },
        {
        "name": "Aaron",
        "email": "goldaaron12@outlook.com",
        "password": "Hola1234"
    },
    {
        "name": "Ame",
        "email": "acristinachan@gmail.com",
        "password": "Adios1234"
    },
]

class User(Resource):
    def get(self, name):
        for user in users:
            if(name == user["name"]):
                return user, 200
        return "User not found", 404

    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("email")
        parser.add_argument("password")
        args = parser.parse_args()

        for user in users:
            if(name == user["name"]):
                return "User with name {} already exists".format(name), 400

        user = {
            "name": name,
            "email": args["email"],
            "password": args["password"]
        }
        users.append(user)
        return user, 201

    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("email")
        parser.add_argument("password")
        args = parser.parse_args()

        for user in users:
            if(name == user["name"]):
                user["email"] = args["email"]
                user["password"] = args["password"]
                return user, 200
        
        user = {
            "name": name,
            "email": args["email"],
            "password": args["password"]
        }
        users.append(user)
        return user, 201

    def delete(self, name):
        global users
        users = [user for user in users if user["name"] != name]
        return "{} is deleted.".format(name), 200
      
api.add_resource(User, "/user/<string:name>")

app.run(debug=True)