from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from article import Article

class sentimenter():
    
    def __init__(self, text):
        text = self.text

    def sentiment_analysis_example(self, client):

        documents = [sentimenter.text]
        response = client.analyze_sentiment(documents=documents)[0]
        print("Document Sentiment: {}".format(response.sentiment))
        print("Overall scores: positive={0:.2f}; neutral={1:.2f}; negative={2:.2f} \n".format(
            response.confidence_scores.positive,
            response.confidence_scores.neutral,
            response.confidence_scores.negative,
        ))
        for idx, sentence in enumerate(response.sentences):
            print("Sentence: {}".format(sentence.text))
            print("Sentence {} sentiment: {}".format(idx+1, sentence.sentiment))
            print("Sentence score:\nPositive={0:.2f}\nNeutral={1:.2f}\nNegative={2:.2f}\n".format(
                sentence.confidence_scores.positive,
                sentence.confidence_scores.neutral,
                sentence.confidence_scores.negative,
            ))
            