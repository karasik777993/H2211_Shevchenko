import sqlite3

connection = sqlite3.connect("IT_DB.sl3", 5)
cur = connection.cursor()
cur.execute("SELECT rowid, name FROM first_teble;")

connection.commit()
res = cur.fetchall()
print(res)
connection.close()