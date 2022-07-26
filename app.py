from flask import Flask, send_from_directory, jsonify, request
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app)

@app.route('/')
def testpage():
    try: 
        return '<h1>Connected to db :)</h1>'
    except Exception as e:
        return '<h1>Not connected to db :(</h1>'
