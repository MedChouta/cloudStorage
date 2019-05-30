from .db import Database
from flask import (request, render_template, flash, redirect, url_for, make_response)
from werkzeug.security import generate_password_hash


class Settings(Database):

    def settings(self, method):
        conn = self.connect(self.DATABASE)
        db = conn.cursor()
        
        userData = db.execute(
            "SELECT first_name, last_name, email FROM user WHERE id=?", (request.cookies.get('user'),)
        ).fetchone()
        print(method)
        if method == "POST":
            if request.form['firstName'] != "":
                self.changeFirstName(db)

            if request.form['lastName'] != "":
                self.changeLastName(db)

            if request.form['email'] != "":
                self.changeEmail(db)

            if request.form['password'] != "":
                self.changePassword(db)
            conn.commit()
            return redirect(url_for('settings'))

        return render_template("settings.html", userData=userData)

    def changeFirstName(self, cursor):
        cursor.execute(
            "UPDATE user SET first_name=? WHERE id=?", (request.form['firstName'], request.cookies.get('user'))
        )

    def changeLastName(self, cursor):
        cursor.execute(
            "UPDATE user SET last_name=? WHERE id=?", (request.form['lastName'], request.cookies.get('user'))
        )

    def changeEmail(self, cursor):
        cursor.execute(
            "UPDATE user SET email=? WHERE id=?", (request.form['email'], request.cookies.get('user'))
        )
        

    def changePassword(self, cursor):
        cursor.execute(
            "UPDATE user SET password=? WHERE id=?", (generate_password_hash(request.form['password']), request.cookies.get('user'))
        )
