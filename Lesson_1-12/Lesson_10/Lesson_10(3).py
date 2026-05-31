import sqlite3

connection = sqlite3.connect("IT_DB.sl3", 5)
cur = connection.cursor()
cur.execute("INSERT INTO first_teble (name) VALUES ('Nick');")
cur.execute("INSERT INTO first_teble (name) VALUES ('Lisa');")

connection.commit()
connection.close()