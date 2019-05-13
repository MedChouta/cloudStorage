import os, sys
from .db import Database
from flask import (request, render_template, flash, redirect, url_for, session, )
from werkzeug import secure_filename

class Dashboard(Database):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DATABASE = os.path.join(BASE_DIR, "database.db")

    def isLogged(self):
        if request.cookies.get('user') is not None:
            return True
        else:
            return redirect(url_for("register"))

    
    def addFile(self, method):
        if method == 'POST':
            f = request.files['file']
            f.save(secure_filename(f.filename))

            with open('text.txt', 'w') as fileo:
                fileo.write(f.filename)
            
            conn  = self.connect(self.DATABASE)
            db = conn.cursor()

            db.execute("INSERT INTO storedFile (fileName, author_id) Values(?, ?)", (f.filename,request.cookies.get('user')))

            conn.commit()
        
            return 'file uploaded successfully'

        else:
            redirect(url_for("dashboard"))

    def showFiles(self):
        if self.isLogged() == True:
            conn  = self.connect(self.DATABASE)
            db = conn.cursor()

            files = db.execute(
                "SELECT F.author_id, F.fileName, F.uploaded FROM storedFile AS F" 
                " INNER JOIN user AS U ON F.author_id=U.id"
            ).fetchall()

            return render_template("dashboard.html")
        else:
            return redirect(url_for('register'))