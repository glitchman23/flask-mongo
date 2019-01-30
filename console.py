from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)


app.config['MONGO_DBNAME'] = 'straint'
app.config["MONGO_URI"] = 'mongodb://localhost:27017/straint'


mongo = PyMongo(app)
users = mongo.db.users

output = users.find({}, { "_id": 1})

for x in output:
	print(x)