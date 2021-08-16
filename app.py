from flask import Flask, render_template, request, url_for, redirect
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import json

app = Flask(__name__)
app.config.from_pyfile('settings.py')
mongo = PyMongo(app)
todos = mongo.db.todos

@app.route('/')
def index():
  return json.dumps({"hello": "world"})

@app.route('/ping')
def ping_server():
  return json.dumps({"ping": "PONG!"})

if __name__ == '__app__':
  app.run(host='0.0.0.0')