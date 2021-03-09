from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

class main():
        
    def authenticate_client(self):
            ta_credential = AzureKeyCredential(key)
            text_analytics_client = TextAnalyticsClient(
                    endpoint=endpoint, 
                    credential=ta_credential)
            return text_analytics_client

    client = authenticate_client()