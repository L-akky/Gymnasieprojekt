import sqlite3

conn = sqlite3.connect("Gyarte_db/ex1.db")
c = conn.cursor()

c.execute("CREATE TABLE ex1(one text, two int)")
c.execute("INSERT INTO ex1 VALUES ('fhem', 10)")

conn.commit()
conn.close()