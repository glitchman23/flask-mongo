from flask import Flask, jsonify, request, render_template, url_for, redirect
from users_model import get_users, insert_user


app = Flask(__name__)


##############################  TEMPLATES  ################################

@app.route('/')
def home():
	return render_template('home.jinja2')


@app.route('/users')
def users():
	output = get_users()
	return render_template('users.jinja2', users=output)


@app.route('/add_user', methods=['POST'])
def add_user():

	name = request.form['name']
	language = request.form['language']
	color = request.form['color']
	age = request.form['age']

	insert_user(name, language, color, age)

	return redirect(url_for('users'))


@app.route('/login')
def auth():
	return render_template('auth.jinja2')



##################################  API  ##################################


@app.route('/users.json', methods=['GET'])
def get_all_users():
	output = get_users()
	return jsonify(output)


if __name__ == '__main__':
	app.run(debug=True)