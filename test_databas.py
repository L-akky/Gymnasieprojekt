import sqlite3
from article import Article
from database import Database

conn = sqlite3.connect("Gyarte_db/gyatre.db")
c = conn.cursor()
a1 = Article()
d1 = Database()

a1.source = "aftonbladet"
a1.title = "Senast nytt om coronaviruset"
a1.url = "https://www.aftonbladet.se/nyheter/a/3Jgxj9/senaste-nytt-om-coronaviruset"
a1.keyword = "corona"
d1.send_to_base(a1)

conn.commit()
conn.close()