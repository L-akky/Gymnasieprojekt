
class Newspaper:
    def __init__(self, newspaper=None):
        if newspaper is None:
            self.__id = 0
            self.__name = ""
            self.__url = ""
        else:
            self.__id = newspaper[0]
            self.__name = newspaper[1]
            self.__url = newspaper[2]

        self.__keywords = []


    def setid(self, id :int):
        self.__id = id
    
    def getid(self):
        return self.__id

    def setname(self, name :str):
        self.__name = name
    
    def getname(self):
        return self.__name

    def seturl(self, url :str):
        self.__url = url

    def geturl(self):
        return self.__url

    def setkeywords(self, keywords :"list_of_keywords"):
        self.__keywords = keywords

    def getkeywords(self):
        return self.__keywords

    id = property(getid, setid)
    name = property(getname, setname)
    url = property(geturl, seturl)
    keywords = property(getkeywords, setkeywords)
