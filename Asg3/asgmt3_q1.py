from google.cloud import language_v2 as lv2
import pandas as pd

cred = "./Cred/t_analysis_key.json"

client = lv2.LanguageServiceClient.from_service_account_json("./Cred/t_analysis_key.json")

df_comments = pd.read_csv("./asg3/Text/Q1_ECHO_COMMENT.csv",encoding='utf-8')

def detect_single_line(text):
    doc = lv2.Document(content=text,type=lv2.Document.Type.PLAIN_TEXT)
    sentiment = client.analyze_sentiment(request={'document': doc}).document_sentiment
    return pd.Series({
        'sentiment': sentiment.score,
        'magnitude': sentiment.magnitude
    })

df_comments[['sentiment','magnitude']] = df_comments['comment'].apply(detect_single_line)

df_comments.to_csv('./asg3/Results/q1.csv',index=False)
