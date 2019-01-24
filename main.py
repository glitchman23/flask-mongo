from flask import Flask, jsonify, request
from flask_pymongo import PyMongo


app = Flask(__name__)


app.config['MONGO_DBNAME'] = 'straint'
app.config["MONGO_URI"] = 'mongodb://localhost:27017/straint'


mongo = PyMongo(app)


@app.route('/users', methods=['GET'])
def get_all_users():
	users = mongo.db.users

	output= []

	for user in users.find():
		output.append({'name' : user['name'], 'language' : user['language'], 'color' : user['color'], 'age' : user['age']})
	return jsonify({ 'result' : output})

@app.route('/users/<name>', methods=['GET'])
def get_one_user(name):
	users = mongo.db.users

	user = users.find_one({'name' : name})

	if user:
		output = {'name' : user['name'], 'language' : user['language'], 'color' : user['color'], 'age' : user['age']}
	else:
		output = 'No results founded'

	return jsonify({'result' : output})

@app.route('/add_user')
def add_one():
	users = mongo.db.users

	name = request.args.get('name')
	language = request.args.get('language')
	color = request.args.get('color')
	age = request.args.get('age')

	if (name == None or language == None or color == None or age == None):
		return jsonify({'result' : 'Missing args'})
	else:
		user_id = users.insert({'name' : name, 'language' : language, 'color' : color, 'age': age})
		new_user = users.find_one({'_id' : user_id})

		output = {'name' : new_user['name'], 'language' : new_user['language'], 'color' : new_user['color'], 'age' : new_user['age'] }

		return jsonify({'result' : output})



if __name__ == '__main__':
	app.run(debug=True)