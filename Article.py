import sqlite3 


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