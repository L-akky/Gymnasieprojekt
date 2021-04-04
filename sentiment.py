from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

class sentimenter:
    

    def sentiment_analysis(self, client, article):

        documents = [article.text]
        response = client.analyze_sentiment(documents=documents)[0] #Anropar API:n
        return response.confidence_scores.positive - response.confidence_scores.negative

    def authenticate_client(self):
        ta_credential = AzureKeyCredential(config([Sentiment.Config][AzureKey]))
        text_analytics_client = TextAnalyticsClient(
            endpoint=config([Sentiment.Conifg][EndPoint]), 
            credential=ta_credential)
        return text_analytics_client

        client = authenticate_client()
        