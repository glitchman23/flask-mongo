from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)


app.config['MONGO_DBNAME'] = 'straint'
app.config["MONGO_URI"] = 'mongodb://localhost:27017/straint'


mongo = PyMongo(app)
users = mongo.db.users

def get_users():

	output= []

	for user in users.find():
		output.append({'name' : user['name'], 'language' : user['language'], 'color' : user['color'], 'age' : user['age']})
	return output

def insert_user(name, language, color, age):

	user_id = users.insert({'name' : name, 'language' : language, 'color' : color, 'age': int(age)})

