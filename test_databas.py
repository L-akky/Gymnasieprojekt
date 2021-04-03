import sqlite3
from newspaper import Newspaper
from storage import Storage

n = Newspaper()
s = Storage()
n.id = None
n.name ="Aftonbladet"
s.save_newspaper(n)
