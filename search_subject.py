
class Search_subject:
     
    def __init__(self, subject=None):
        if subject is None:
            self.__id = 0
            self.__text = ""

        else:
            self.__id = subject[0]
            self.__text = subject[1]

    def setid(self, id :int):
        self.__id = id
    
    def getid(self):
        return self.__id
    

    def settext(self, text :str):
        self.__text = text
    
    def gettext(self):
        return self.__text


    id = property(getid, setid)
    text = property(gettext, settext)