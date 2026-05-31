import sqlite3

connection = sqlite3.connect("IT_DB.sl3", 5)
cur = connection.cursor()
cur.execute("UPDATE first_teble SET name='Kate' WHERE rowid=3")

connection.commit()
connection.close()