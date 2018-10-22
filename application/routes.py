from flask import render_template
from application import application

@application.route('/')
@application.route('/index')
def index():
	user = {'username' : 'Rohit Pandey'}
	posts= [
		{
			'author':{'username' : 'Suri'},
			'body' : 'I say meow!'
		},
		{
			'author':{'username' : 'Noell'},
			'body' : 'Me too!'
		}
	]
	return render_template('index.html', title='Home', user=user, posts=posts)

