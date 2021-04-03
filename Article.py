
class Article:

    def __init__(self, article=None):
        if article is None:
            self.__id = None
            self.__keyword_id = None
            self.__text = ""
            self.__sentiment = None
        else:
            self.__id = article[0]
            self.__keyword_id = article[1]
            self.__text = article[2]
            self.__sentiment = article[3]

    def setid(self, id :int):
        self.__id = id
    
    def getid(self):
        return self.__id

    def setkeyword_id(self, keyword_id :int):
        self.__keyword_id = keyword_id

    def getkeyword_id(self):
        return self.__keyword_id
    
    def settext(self, text :str):
        self.__text = text

    def gettext(self):
        return self.__text

    def setsentiment(self, sentiment :float):
        self.__sentiment = sentiment
    
    def getsentiment(self):
        return self.__sentiment
    
    id = property(getid, setid)
    keyword_id=property(getkeyword_id, setkeyword_id)
    text=property(gettext, settext)
    sentiment=property(getsentiment, setsentiment)