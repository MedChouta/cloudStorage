import sqlite3
from sqlite3 import Error


class Database:
	
	def __init__(dbFile):
	
	
	def connect(dbFile):
		try:
			db = sqlite3(dbFile)
			return db
		except Error as e:
			print(e)
		return None
	
	def close(db):
		db.close()
		