from flask import (Flask, request, g, make_response)
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
	if request.method == 'GET':
		return dashB.showFiles()
	else:
		return dashB.addFile(request.method)

@app.route('/check')
def check():
	return request.cookies.get('user')