from texttable import Texttable
from storage import Storage
from article import Article
from sentiment import sentimenter
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

def update():
        sg = Storage()
        sm = sentimenter()
        newspapers = sg.get_newspapers()
        
        for newspaper in newspapers:
                print(newspaper.name)
                newspaper.keywords = sg.get_keywordmappings(newspaper.id)
                
                for keyword in newspaper.keywords:
                        print(keyword.text)
                        keyword.articles = sg.get_articles(keyword.keyword_mapping_id)
                        
                        for article in keyword.articles:
                                if article.sentiment is None:
                                        client = sm.authenticate_client()
                                        if len(article.text) > config([Main.Config][MinValue]):
                                                if len(article.text) >= config([Main.Config][MaxValue]):
                                                        article.text = article.text[:config([Main.Config][CutValue])]
                                                article.sentiment = sm.sentiment_analysis(client, article)
                                                if keyword.avg_sentiment is None:
                                                        keyword.avg_sentiment = 0
                                                keyword.avg_sentiment = (keyword.avg_sentiment * (len(keyword.articles) - 1) + article.sentiment) / len(keyword.articles)
                                                print(article.sentiment, keyword.avg_sentiment)
                                                sg.save_article(article)
                                        else:
                                                article.sentiment = 0
                        sg.save_keyword(keyword)
              
def make_table():
        t = Texttable()
        sg = Storage()
        newspapers = sg.get_newspapers()
        keywords = sg.get_all_keywords()
        papers = ['Newspapers/Keywords']
        for keyword in keywords:
                print(keyword.text)

        for newspaper in newspapers:
                papers.append(newspaper.name)
        t.add_rows([papers])
        
        for keyword in keywords:
                
                data = [keyword.text]
                for newspaper in newspapers:
                        keywordmapping = sg.get_keywordnewspaper_mapping(newspaper.id, keyword.id)
                        print(keyword.text, newspaper.name, keywordmapping.avg_sentiment)
                        if keywordmapping.avg_sentiment is not None:
                                data.append(keywordmapping.avg_sentiment)
                        else:
                                data.append("*")
        
                        print("keywordmapping")
                print(data)
                t.add_row(data)
        
        print(t.draw())



update()
make_table()

