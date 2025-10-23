from google.cloud import language_v2 as lv2
import pandas as pd

cred = "./Cred/t_analysis_key.json"

client = lv2.LanguageServiceClient.from_service_account_json("./Cred/t_analysis_key.json")

q2_text = str(
    'The Chinese University of Hong Kong (CUHK) Business School welcomed more than 750 new undergraduates from 20 locations around the world into CUHK Business School family at our Inauguration Ceremony on 24 August. This signature event celebrated the start of an exciting new chapter for our incoming class, marking the beginning of their academic and personal growth within our vibrant community.'
)



def detect_entities(text):
    document = lv2.Document(content=text, type_=lv2.Document.Type.PLAIN_TEXT)
    response = client.analyze_entities(document=document, encoding_type=lv2.EncodingType.UTF8)
    print(response)
    data = []
    for entity in response.entities:
        entity_name = entity.name
        entity_type = lv2.Entity.Type(entity.type_).name  # 转为字符串
                             # 重要性得分
        entity_probability = entity.mentions[0].probability

        # 收集数据
        data.append({
            "entity_name": entity_name,
            "entity_type": entity_type,
            "probability": entity_probability
        })

    # 转换为 DataFrame
    df_entities = pd.DataFrame(data)

    return df_entities

df_entities = detect_entities(text=q2_text)
df_ent_is_person = df_entities[df_entities['entity_type'] == 'PERSON']
df_ent_high_prob = df_entities[df_entities['probability'] > 0.01]

# print(df_entities.to_string())
print(df_ent_is_person)
# detect_entities(q2_text).to_csv('./asg3/Results/q2.csv',index=False)

