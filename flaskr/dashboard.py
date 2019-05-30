import os, sys, math
from .db import Database
from flask import (request, render_template, flash, redirect, url_for, session, )
from werkzeug import secure_filename

class Dashboard(Database):
    UPLOAD_FOLDER = "C:\\Users\\mohammed\\project\\flaskr\\static\\uploads"

    def showFiles(self, method):
        if request.cookies.get('user') is not None:

            count = self.countFiles()
            user = self.getUser()

            if method == "GET":        
                conn  = self.connect(self.DATABASE)
                db = conn.cursor()

                files = db.execute(
                        "SELECT F.id, F.author_id, F.fileName, F.uploaded FROM storedFile AS F" 
                        " INNER JOIN user AS U ON F.author_id=U.id"
                ).fetchall()

                conn.commit()
                
                return render_template("dashboard.html", files=files, uploads=self.UPLOAD_FOLDER, count=count[0], username=user[1])
            
            else:
                if 'extensions' in request.form:
                    print("[MC]OUTPUT")
                    files = self.filter()
                    return render_template("dashboard.html", files=files, uploads=self.UPLOAD_FOLDER, count=count[0], username=user[1])
                elif 'order' in request.form:
                    files = self.order()
                    return render_template("dashboard.html", files=files, uploads=self.UPLOAD_FOLDER, count=count[0], username=user[1])
                elif 'search' in request.form:
                    files = self.search()
                    return render_template("dashboard.html", files=files, uploads=self.UPLOAD_FOLDER, count=count[0], username=user[1])
                else:
                    return self.addFile(method)

        else:
            return redirect(url_for('root'))

    def addFile(self, method):
        if method == 'POST':
            f = request.files['file']
            fileName = secure_filename(f.filename)
            f.save(os.path.join(self.UPLOAD_FOLDER, fileName))
            
            extension = fileName.split('.')
            extension = extension[len(extension)-1]
            
            print(extension)

            conn  = self.connect(self.DATABASE)
            db = conn.cursor()

            uniqFile = db.execute("SELECT * FROM storedFile WHERE fileName=?", (fileName,)).fetchone()
            
            if uniqFile is not None:
                db.execute("DELETE FROM storedFile WHERE fileName=?", (fileName,))
            
            db.execute("INSERT INTO storedFile (fileName, author_id, extension) Values(?, ?, ?)", (f.filename, request.cookies.get('user'), extension))
            
            conn.commit()
        
            return redirect(url_for('dashboard'))

        else:
            return redirect(url_for("dashboard"))

    def countFiles(self):
        conn = self.connect(self.DATABASE)
        db = conn.cursor()

        count = db.execute(
            "SELECT COUNT(*) FROM storedFile WHERE author_id=?", (request.cookies.get('user'),)
        ).fetchone()

        conn.commit()

        return count

    def getUser(self):
        conn = self.connect(self.DATABASE)
        db = conn.cursor()

        user = db.execute(
            "SELECT * FROM user WHERE id=?", (request.cookies.get('user'),)
        ).fetchone()

        conn.commit()

        return user

    def delete(self, post_id):
        conn = self.connect(self.DATABASE)
        db = conn.cursor()

        file2delete = db.execute(
            "SELECT * FROM storedFile WHERE id=?", (post_id,)
        ).fetchone()

        if file2delete is None:
            return "Cannot delete this file"
        
        db.execute(
            "DELETE FROM storedFile WHERE id=? AND author_id=?", (post_id, request.cookies.get('user'))
        )
        
        conn.commit()

        return redirect(url_for('dashboard'))


    def order(self):
        conn  = self.connect(self.DATABASE)
        db = conn.cursor()
        order = request.form['order']
        
        if order == "ASC" or order == "DESC":
            files = db.execute(
                "SELECT F.id, F.author_id, F.fileName, F.uploaded FROM storedFile AS F" 
                " INNER JOIN user AS U ON F.author_id=U.id ORDER BY F.uploaded " + order
            ).fetchall()
        else:
            files = db.execute(
                "SELECT F.id, F.author_id, F.fileName, F.uploaded FROM storedFile AS F" 
                " INNER JOIN user AS U ON F.author_id=U.id ORDER BY F.fileName ASC"
            ).fetchall()

        conn.commit()

        return files
        
    def filter(self):
        conn  = self.connect(self.DATABASE)
        db = conn.cursor()
        ext = request.form['extensions']
        
        files = db.execute(
                "SELECT id, author_id, fileName, uploaded FROM storedFile WHERE author_id=? AND (extension=? OR extension=upper(?))", (request.cookies.get('user'), ext, ext)
                ).fetchall()
        print(files)


        conn.commit()

        return files

    def search(self):
        conn = self.connect(self.DATABASE)
        db = conn.cursor()
        query = request.form['search']

        files = db.execute(
            "SELECT id, author_id, fileName, uploaded FROM storedFile WHERE fileName LIKE ?", (query+'%',)
        ).fetchall()

        return files