from flask import (Flask, request, g, make_response, redirect, url_for, render_template)
from .auth import Auth
from .dashboard import Dashboard
from .settings import Settings

app = Flask(__name__)
app.secret_key = "dev"

auth = Auth()
dashB = Dashboard()
sett = Settings()

@app.route('/', methods=('GET', 'POST'))
def root():
	if 'user' not in request.cookies:
		if request.method == "POST":
			if "register" in request.form:
				return auth.register(request.method)
			elif "login" in request.form:
				return auth.login(request.method)
		else:
			return render_template("register.html")
	else:
		return redirect(url_for('dashboard'))
 
	
@app.route('/dashboard', methods=('GET', 'POST'))
def dashboard():
	return dashB.showFiles(request.method)

@app.route('/dashboard/settings', methods=('GET', 'POST'))
def settings():
	return sett.settings(request.method)

@app.route('/delete/<int:post_id>')
def delete(post_id):
	return dashB.delete(post_id)

@app.route('/logout')
def logout():
	return auth.logout()