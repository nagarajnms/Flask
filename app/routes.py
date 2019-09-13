from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
	user = {'username': 'Nagaraj'}
	posts = [
		{
			'author': {'name': 'Rose'},
		 	'message': 'Lovely Weather.!'
		},
		{
			'author': {'name': 'Mahesh'},
		 	'message': 'I stay in India.'
		}
	]
	return render_template('index.html', title = 'Home', user = user, posts = posts)