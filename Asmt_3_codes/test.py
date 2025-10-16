from google.cloud import language_v2

client = language_v2.LanguageServiceClient.from_service_account_json("./Cred/t_analysis_key.json")

def sentiment_detect(thetext):
    document = language_v2.Document(content=thetext, type_=language_v2.Document.Type.PLAIN_TEXT) # Create a Document object from the input text, specifying it as plain text
    sentiment = client.analyze_sentiment(request={'document': document}).document_sentiment
    return(sentiment)

def sentiment_detect_by_text(text_filepath):
    