import sqlite3 

class Database:
    def __init__(self):
        pass

    def send_to_base(self, a: "Article" ):
            conn = sqlite3.connect("Gyarte_db/gyatre.db")
            c = conn.cursor()
            value_list = (a.source, a.title, a.url, a.keyword, a.text)
            c.execute("INSERT INTO Artiklar VALUES(?,?,?,?,?)", value_list)
            conn.commit()
            conn.close()
    