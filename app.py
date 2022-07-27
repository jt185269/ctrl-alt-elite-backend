from flask import Flask, send_from_directory, jsonify, request, send_file
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
import json
import ast
import sys

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
def login():
    if request.method == 'POST':
        try:
            req = ast.literal_eval(request.data.decode('utf-8'))
            myUser = req['Email']
            myPass = req['Password']
            thisUser = {
                "userID" : 1,
                "name" : "James",
                "email" : "James@James.com",
                "password" :  "password",
                "companyID" : 1
            }

            if myUser == thisUser["email"] and myPass == thisUser["password"]:
                return { "auth" : True } 
            else:
                return { "auth" : False }
        except: 
            raise Exception("Failed to login")


@app.route('/api/datafetch', methods=['GET', 'POST'])
def dataFetch():
    if request.method == 'GET':
        try:
            with open("./data.json", 'r') as f:
                data = f.read()
            companyData = json.dumps(data)
            return (companyData)
        except: 
            raise Exception("Failed to load file")
