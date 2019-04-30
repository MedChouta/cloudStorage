from flask import Flask
from .auth import Auth
from .dashboard import Dashboard

app = Flask(__name__)

auth = Auth()
dashB = Dashboard()


@app.route('/')
def showHome():
	home.showHome()

@app.route('/register')
def showRegister():
	auth.showRegister()

@app.route('/login')
def showLogin():
	auth.showLogin()
	
@app.route('/dashboard')
def showDashboard():
	dashB.showDashboard


