import sqlite3 
from article import Article
from sentiment_mock import Sentimenter_mock

class Database:
    def __init__(self):
        self.articles = ""

    def send_to_base(self, a: "Article" ):
        conn = sqlite3.connect("Gyarte_db/gyatre.db")
        c = conn.cursor()
        s1 = Sentimenter_mock()
        value_list = (a.source, a.title, a.url, a.keyword, a.text, s1.get_sentiment()[0], s1.get_sentiment()[1], s1.get_sentiment()[0])
        print("Inserting values")
        c.execute("INSERT INTO Articles VALUES(?,?,?,?,?,?,?,?)", value_list)
        c.execute("SELECT * FROM Articles")
        print("Values inserted")
        conn.commit()
        conn.close()
        print("Commited and closed")
    
    def get_articles(self, subject, newspaper):
        conn = sqlite3.connect("Gyarte_db/gyatre.db")
        c = conn.cursor()
        print("Getting articles")
        c.execute("SELECT Source, Title, URL, Keyword, Text, Positive_Sentiment, Neutral_Sentiment, Negative_Sentiment FROM Articles WHERE Keyword=?", (subject,))
        print("executed")
        self.article = c.fetchall()
        print(self.article)
        print("Got articles")
        conn.close()
        print("Closed")