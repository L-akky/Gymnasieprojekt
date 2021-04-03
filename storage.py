import sqlite3 
from article import Article
from newspapers import Newspaper
from subject import Subject
from search_subject import Search_subject

class Storage:
    def __init__(self):
        self.articles = ""
        self.keywords = ""

    def get_newspapers(self):
        conn = sqlite3.connect("Gyarte_db/gyarte.db")
        c = conn.cursor()
        c.execute(("SELECT ID, Name, Url FROM Newspaper"))
        newspapers = c.fetchall()
        stored_papers = []
        for np in newspapers:
            stored_papers.append(Newspaper(np))
            
        conn.close()
        return stored_papers
    
    def get_all_keywords(self):
        conn = sqlite3.connect("Gyarte_db/gyarte.db")
        c = conn.cursor()
        c.execute("SELECT ID, Name FROM Keyword")
        keywords = c.fetchall()
        stored_keywords = []
        for kw in keywords:
            stored_keywords.append(Search_subject(kw))

        conn.close()
        return stored_keywords
        
    def get_keywords(self, newspaperID):
        conn = sqlite3.connect("Gyarte_db/gyarte.db")
        c = conn.cursor()
        c.execute("SELECT Keyword.ID, KeywordNewspaperMapping.ID as KeywordMappingID, NewspaperID, Name, Avg_sentiment FROM KeywordNewspapermapping JOIN Keyword on Keyword.ID = KeywordNewspaperMapping.KeywordID where NewspaperID=?", (newspaperID,))
        keywords = c.fetchall()
        stored_keywords = []
        for kw in keywords:
            stored_keywords.append(Subject(kw))

        conn.close()
        return stored_keywords
    
    def get_keywordnewspaper_mapping(self, newspaperID, keywordID):
        conn = sqlite3.connect("Gyarte_db/gyarte.db")
        c = conn.cursor()
        c.execute("SELECT Keyword.ID, KeywordNewspaperMapping.ID as KeywordMappingID, NewspaperID, Name, Avg_sentiment FROM KeywordNewspapermapping JOIN Keyword on Keyword.ID = KeywordNewspaperMapping.KeywordID where NewspaperID=? AND KeywordID=?", (newspaperID, keywordID))
        keyword = Subject(c.fetchone())
        conn.close()
        return keyword

    def get_articles(self, keywordID):
        conn = sqlite3.connect("Gyarte_db/gyarte.db")
        c = conn.cursor()
        c.execute("SELECT ID, KeywordID, Content, Sentiment FROM Article WHERE KeywordID=?", (keywordID,))
        articles = c.fetchall()
        stored_articles = []
        for ac in articles:
            stored_articles.append(Article(ac))

        conn.close()
        return stored_articles
    
    def get_unevaluated_articles(self, keywordID):
        conn = sqlite3.connect("Gyarte_db/gyarte.db")
        c = conn.cursor()
        c.execute("SELECT ID, KeywordID, Content, Sentiment FROM Article WHERE KeywordID=? AND sentiment is NULL", (keywordID,))
        articles = c.fetchall()
        stored_articles = []
        for ac in articles:
            stored_articles.append(Article(ac))

        conn.close()
        return stored_articles

    def get_articles_by_keyword_and_paper(self, keywordID, newspaperID):
        conn = sqlite3.connect("Gyarte_db/gyarte.db")
        c = conn.cursor()
        c.execute("SELECT article.ID, KeywordID, Content, Sentiment FROM Article join KeywordNewspaperMapping knm on knm.ID= article.KeywordID WHERE knm.KeywordID=? AND knm.NewspaperID=?", (keywordID, NewspaperID))
        articles = c.fetchall()
        stored_articles = []
        for ac in articles:
            stored_articles.append(Article(ac))

        conn.close()
        return stored_articles

    def save_newspaper(self, newspaper):
        conn = sqlite3.connect("Gyarte_db/gyarte.db")
        c = conn.cursor()
        if newspaper.id == None:
            data = (newspaper.id, newspaper.name)
            c.execute("INSERT INTO Newspaper VALUES(?,?)", data)

        else:
            data = (newspaper.name, newspaper.id)
            c.execute("UPDATE Newspaper set Name=? where id=?", data)

        conn.commit()
        conn.close()

    def save_keyword(self, keyword):
        conn = sqlite3.connect("Gyarte_db/gyarte.db")
        c = conn.cursor()
        if keyword.id == None:
            data =(keyword.id, keyword.newspaper_id, keyword.avg_sentiment, keyword.keyword_mapping_id)
            c.execute("INSERT INTO KeywordNewspaperMapping VALUES(?,?,?,?)", data)

        else:
            data =(keyword.newspaper_id, keyword.id, keyword.avg_sentiment, keyword.keyword_mapping_id)
            c.execute("UPDATE or IGNORE KeywordNewspaperMapping set NewspaperID=?, KeywordID=?, Avg_Sentiment=?, ID=?", data)

        conn.commit()
        conn.close()

    def save_article(self, article):
        conn = sqlite3.connect("Gyarte_db/gyarte.db")
        c = conn.cursor()
        if article.id == None:
            data = (article.id, article.keyword_id, article.text, article.sentiment)
            c.execute("INSERT INTO article VALUES(?,?,?,?)", data)

        else:
            data = (article.keyword_id, article.text, article.sentiment, article.id)
            c.execute("UPDATE article set KeywordID=?, Content=?, Sentiment=? where ID=?", data)

        conn.commit()
        conn.close()
