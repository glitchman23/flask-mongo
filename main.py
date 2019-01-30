from flask import Flask, jsonify, request, render_template, url_for, redirect, flash
from forms import RegistrationForm, LoginForm
from users_model import get_users, insert_user


app = Flask(__name__)

app.config['SECRET_KEY'] = '92d55cfc39b5c5a115ff84baebd0b834'


##############################  TEMPLATES  ################################

@app.route('/')
@app.route('/home')
def home():
	return render_template('home.jinja2')


@app.route('/users')
def users():
	output = get_users()
	return render_template('users.jinja2', users=output, title='Users')


@app.route('/add_user', methods=['POST'])
def add_user():

	name, language, color, age = (request.form['name'], request.form['language'], request.form['color'], request.form['age'])

	insert_user(name, language, color, age)

	return redirect(url_for('users'))

@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f'Account created for {form.username.data}!', 'success')
		return redirect(url_for('home'))
	return render_template('register.jinja2', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.email.data == 'admin@straint.com' and form.password.data == 'password':
			flash(f'You have been logged in!', 'success')
			return redirect(url_for('home'))
		else:
			flash(f'Login unsuccessful. Please check username and password', 'danger')

	return render_template('login.jinja2', title='Login', form=form)


##################################  API  ##################################


@app.route('/users.json', methods=['GET'])
def get_all_users():
	output = User.get_users()
	return jsonify(output)


if __name__ == '__main__':
	app.run(debug=True)