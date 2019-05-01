import sqlite3
from sqlite3 import Error


class Database:
	
	def connect(self, dbFile):
		try:
			db = sqlite3.connect(dbFile)
			return db
		except Error as e:
			print(e)
		return None
	
	def close(self, db):
		db.close()
		