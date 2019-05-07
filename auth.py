import os
from .db import Database
from flask import (request, render_template, flash, redirect, url_for)
from werkzeug.security import check_password_hash, generate_password_hash


class Auth(Database):
	BASE_DIR = os.path.dirname(os.path.abspath(__file__))
	DATABASE = os.path.join(BASE_DIR, "database.db")

	def register(self, method):
		if method == "POST":
			conn = self.connect(self.DATABASE)
			db = conn.cursor()


			firstName = request.form['firstName']
			lastName = request.form['lastName']
			email = request.form['email']
			password = request.form['password']
			error = None

			if not (firstName or lastName or email or password):
				error = 'All inputs are required'
			elif db.execute('SELECT id FROM user WHERE email = ?', (email,)).fetchone() is not None: #checks if the specified email is already registered
				error = 'this email is already registered.'

			if error is None:
				db.execute(
					'INSERT INTO user (first_name, last_name, email, password) Values(?, ?, ?, ?)',
					(firstName, lastName, email, generate_password_hash(password))
				)
				conn.commit()
				return redirect(url_for('login'))
			
			flash(error)

		return render_template("register.html")

	def login(self, method):
		if method == "POST":
			conn = self.connect(self.DATABASE)
			db = conn.cursor()

			email = request.form['email']
			password = request.form['password']
			error = None
			user  = db.execute('Select * from user WHERE email = ?', (email,))

			if not (email or password):
				error = "Please fill every input"

			if user is None:
				error = "Incorrect email"
			elif not check_password_hash(user['password'], password):
				error = "Incorrect password"

			if error is None:
				session.clear()
				session['user_id'] = user['id']
				return redirect(url_for('dashboard'))

			flash(error)

		return render_template('register.html')

	def logout(self):
		session.clear()
		return redirect(url_for(home))