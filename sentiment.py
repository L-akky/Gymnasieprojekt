from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential


class sentimenter():
    

    def sentiment_analysis(self, client, article):

        documents = [article.text]
        response = client.analyze_sentiment(documents=documents)[0]
        return response.confidence_scores.positive - response.confidence_scores.negative

    def authenticate_client(self):
        ta_credential = AzureKeyCredential("d2a1685d47e64ad38e3f2d43b4bd4750")
        text_analytics_client = TextAnalyticsClient(
            endpoint="https://sentimenter.cognitiveservices.azure.com/", 
            credential=ta_credential)
        return text_analytics_client

        client = authenticate_client()
        