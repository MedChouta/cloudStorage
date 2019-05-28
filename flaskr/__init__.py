from flask import (Flask, request, g, make_response, redirect, url_for)
from .auth import Auth
from .dashboard import Dashboard

app = Flask(__name__)
app.secret_key = "dev"

auth = Auth()
dashB = Dashboard()

@app.route('/register', methods=('GET', 'POST'))
def register():
	return auth.register(request.method)

@app.route('/login', methods=('GET', 'POST'))
def login():
	return auth.login(request.method)
	
@app.route('/dashboard', methods=('GET', 'POST'))
def dashboard():
		return dashB.showFiles(request.method)

@app.route('/delete/<int:post_id>')
def delete(post_id):
	return dashB.delete(post_id)

@app.route('/logout')
def logout():
	return auth.logout()

"""
@app.before_request
def before_request():
	if request.cookies.get('user') is None:
		return redirect(url_for('login'))
	elif (request.cookies.get('user') is not None) and request.endpoint != 'dashboard':
		return redirect(url_for('dashboard'))"""