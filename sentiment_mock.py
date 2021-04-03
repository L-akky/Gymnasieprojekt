from random import uniform

class Sentimenter_mock:
    def __init__(self):
        self.positive_sentiment = 0.0
        self.neutral_sentiment = 0.0
        self.negative_sentiment = 0.0

    def sentiment_analysis(self, client, article):
            documents = [article.text]
            print("Crunching the numbers")
            self.positive_sentiment = uniform(0.0,1.0)
            self.neutral_sentiment = uniform(0.0,1.0)
            self.negative_sentiment = uniform(0.0,1.0)
            print(documents)
            print("Overall scores: Positive={0:.2f}; Neutral={1:.2f}; Negative={2:.2f} \n".format(
                self.positive_sentiment,
                self.neutral_sentiment,
                self.negative_sentiment,
            ))
            return self.positive_sentiment - self.negative_sentiment     
        
    def get_sentiment(self):
        return [self.positive_sentiment, self.neutral_sentiment, self.negative_sentiment]


