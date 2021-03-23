import sqlite3
from random import uniform
from database import Database

class Sentimenter_mock:
    def __init__(self):
        self.positive_sentiment = ""
        self.neutral_sentiment = ""
        self.negative_sentiment =""


    def sentiment_analysis(self, client, subject, newspaper):
            db = Database()
            documents = [db.get_text(subject, newspaper)]
            print(documents)
            print("Overall scores: Positive={0:.2f}; Neutral={1:.2f}; Negative={2:.2f} \n".format(
                positive_awnser,
                neutral_awnser,
                negative_awnser,
            ))
    
    def get_sentiment(self):
        self.positive_sentiment = uniform(0.0,1.0)
        self.neutral_sentiment = uniform(0.0,1.0)
        self.negative_sentiment = uniform(0.0,1.0)
        return [self.positive_sentiment, self.neutral_sentiment, self.negative_sentiment]


