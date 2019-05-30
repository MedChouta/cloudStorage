import sqlite3, os
from sqlite3 import Error


class Database:

	BASE_DIR = os.path.dirname(os.path.abspath(__file__))
	DATABASE = os.path.join(BASE_DIR, "database.db")

	def connect(self, dbFile):
		try:
			db = sqlite3.connect(dbFile)
			return db
		except Error as e:
			print(e)
		return None
	
	def close(self, db):
		db.close()
		