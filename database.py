import sqlite3 
from article import Article
class Database:
    def __init__(self):
        self.text = ""

    def send_to_base(self, a: "Article" ):
        conn = sqlite3.connect("Gyarte_db/gyatre.db")
        c = conn.cursor()
        value_list = (a.source, a.title, a.url, a.keyword, a.text, "", "", "") #"" är temporärt tills jag har skapat fake senitimenter
        print("Inserting values")
        c.execute("INSERT INTO Articles VALUES(?,?,?,?,?,?,?,?)", value_list)
        c.execute("SELECT * FROM Articles")
        print("Values inserted")
        conn.commit()
        conn.close()
        print("Commited and closed")
    
    def get_text(self, subject, newspaper):
        conn = sqlite3.connect("Gyarte_db/gyatre.db")
        c = conn.cursor()
        print("Getting text")
        c.execute("SELECT Source, Title, URL, Keyword, Text, Positive_Sentiment, Neutral_Sentiment, Negative_Sentiment FROM Articles WHERE Keyword=?" (subject,))
        self.text = c.fetchall()
        print("Got text")
        conn.close()
        print("Closed")