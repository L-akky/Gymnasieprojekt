
class Subject:

    def __init__(self, subject=None):
        if subject is None:
            self.__id = 0
            self.__keyword_mapping_id = 0
            self.__newspaper_id = 0
            self.__text = ""
            self.__avg_sentiment = None
        else:
            self.__id = subject[0]
            self.__keyword_mapping_id = subject[1]
            self.__newspaper_id = subject[2]
            self.__text = subject[3]
            self.__avg_sentiment = subject[4]
            
        self.__articles = []

    def setid(self, id :int):
        self.__id = id
    
    def getid(self):
        return self.__id
    
    def setkeyword_mapping_id(self, keyword_mapping_id :int):
        self.__keyword_mapping_id = keyword_mapping_id
    
    def getkeyword_mapping_id(self):
        return self.__keyword_mapping_id

    def setnewspaper_id(self, newspaper_id :int):
        self.__newspaper_id = newspaper_id
    
    def getnewspaper_id(self):
        return self.__newspaper_id

    def settext(self, text :str):
        self.__text = text
    
    def gettext(self):
        return self.__text

    def setavg_sentiment(self, avg_sentiment :float):
        self.__avg_sentiment = avg_sentiment
    
    def getavg_sentiment(self):
        return self.__avg_sentiment

    def setarticles(self, articles :"list_of_articles"):
        self.__articles = articles

    def getarticles(self):
        return self.__articles

    id = property(getid, setid)
    text = property(gettext, settext)
    keywords = property(getarticles, setarticles)
    newspaper_id = property(getnewspaper_id, setnewspaper_id)
    avg_sentiment = property(getavg_sentiment, setavg_sentiment)
    keyword_mapping_id = property(getkeyword_mapping_id, setkeyword_mapping_id)
    