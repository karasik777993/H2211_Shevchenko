import sqlite3

connection = sqlite3.connect("IT_DB.sl3", 5)
cur = connection.cursor()
cur.execute("INSERT INTO first_teble (name) VALUES ('Anna');")
cur.execute("INSERT INTO first_teble (name) VALUES ('John');")

connection.commit()
cur.execute("SELECT rowid, name FROM first_teble;")

res = cur.fetchall()
print(res)
connection.close()