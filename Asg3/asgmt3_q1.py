from google.cloud import language_v2
import pandas as pd

cred = "./Cred/"

client = language_v2.LanguageServiceClient()

text = pd.read_csv("./Text/Q1_ECHO_COMMENT.csv",encoding='utf-8')

print(text)
