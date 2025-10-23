from google.cloud import vision
import pandas as pd
import os
import re

cred = "./Cred/t_analysis_key.json"
client = vision.ImageAnnotatorClient.from_service_account_json(cred)

def get_file_content(filePath):
    with open(filePath,'rb') as fp:
        return fp.read()

def image_label_detect(image_file):
    image = vision.Image(content=image_file)
    response = client.label_detection(image=image)
    return response

def batch_image_labeling(image_folder_path):
    data = []
    # 遍历目录中的所有文件
    for filename in os.listdir(image_folder_path):
        file_path = os.path.join(image_folder_path, filename)
        image_content = get_file_content(file_path)

        # 调用识别函数
        response = image_label_detect(image_content)
        print(response)
        # 提取数字索引，例如 img12.png → 12
        match = re.search(r'\d+', filename)
        index = int(match.group()) if match else None

        label_dict = {
                label.description: round(label.score, 3)
                for label in response.label_annotations
                if label.score >= 0.8
            }

            # 只保留得分高的标签
        data.append({
                "index": index,
                "filename": filename,
                "results": label_dict
            })

    # 转为 DataFrame
    df = pd.DataFrame(data)

    # 以 index 作为索引列
    df.set_index("index", inplace=True)
    df.sort_index(inplace=True)
    df.to_csv('./asg3/results/q3', encoding='utf-8', index=True)

    return df

df = batch_image_labeling('./Asg3/Pics')
print(df.to_string())