from flask import Flask, send_from_directory, jsonify, request
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app)

@app.route('/')
def testpage():
    try: 
        return {
            "text": "Hello from server :)"
        }
    except Exception as e:
        return {
            "text": "hmm, something went wrong rip :(("
        }

@app.route('/api/login', methods=['GET', 'POST'])
def login(user):
    thisUser = {
        "userID" : 1,
        "name" : "James",
        "email" : "James@James.com",
        "password" :  "password",
        "companyID" : 1
    }

    if (user.email == thisUser["email"] and user.password == thisUser["password"]):
        return {
            "auth" : True
        } 
    else:
        return {
        "auth" : False
    }
