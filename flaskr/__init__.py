from flask import (Flask, request)
from .auth import Auth
#from .dashboard import Dashboard



app = Flask(__name__)
auth = Auth()
#dashB = Dashboard()

@app.route('/register', methods=('GET', 'POST'))
def register():
	return auth.register(request.method)

@app.route('/login', methods=('GET', 'POST'))
def login():
	return auth.login(request.method)
	
@app.route('/dashboard')
def dashboard():
	pass


