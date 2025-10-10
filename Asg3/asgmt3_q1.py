from google.cloud import language_v2 as lv2
import pandas as pd

cred = "./Cred/t_analysis_key.json"

client = lv2.LanguageServiceClient.from_service_account_json("./Cred/t_analysis_key.json")

df_comments = pd.read_csv("./asg3/Text/Q1_ECHO_COMMENT.csv",encoding='utf-8')

def detect_single_line(text):
    doc = lv2.Document(content=text,type=lv2.Document.Type.PLAIN_TEXT)
    sentiment = client.analyze_sentiment(request={'document': doc}).document_sentiment
    return sentiment

for comment in df_comments['comment']:
    index = 0
    sentiment_result = detect_single_line(str(comment))
    comment_sentiment = sentiment_result.score
    comment_stmt_magnitude = sentiment_result.magnitude
    df_comments['sentiment'][index] = comment_sentiment
    df_comments['magnitude'][index] = comment_stmt_magnitude
    index += 1

df_comments.to_csv('./asg3/Results/q1.csv',index=False)
