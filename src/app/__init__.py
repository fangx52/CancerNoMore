from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://127.0.0.1:27017/noteattude"
mongo = PyMongo(app)

from app import routes