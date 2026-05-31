import sqlite3

connection = sqlite3.connect("IT_DB.sl3", 5)
cur = connection.cursor()
cur.execute("CREATE TABLE first_teble (name TEXT);")

connection.commit()
connection.close()