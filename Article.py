import sqlite3 
conn = sqlite3.connect("Gyarte_db/gyatre.db")
c = conn.cursor()

class Article:

    def __init__(self):
        self.__source = ""
        self.__title = ""
        self.__url = ""
        self.__keyword = ""

    def setsource(self, source):
        self.__source = source

    def getsource(self):
        return self.__source

    def settitle(self, title):
        self.__title = title

    def gettitle(self):
        return self.__title

    def seturl(self, url):
        self.__url = url

    def geturl(self):
        return self.__url

    def setkeyword(self, keyword):
        self.__keyword = keyword

    def getkeyword(self):
        return self.__keyword

    source=property(getsource, setsource)
    title=property(gettitle, settitle)
    url=property(geturl, seturl)
    keyword=property(getkeyword, setkeyword)
    
    value_list = [getsource(), gettitle(), geturl(), getkeyword()]

    def send_to_base(self):
        if c.fetchone()[0]== 1:
            for values in value_list:
                c.execute("INSERT INTO Artiklar VALUES(?,?,?,?)", values)
            
        else:
            c.execute("CREATE TABLE Artiklar(Source text, Title text, URL blob, Keyword text)")