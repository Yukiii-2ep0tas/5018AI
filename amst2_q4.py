import json
from googleapiclient.discovery import build
import csv

f_API = open("./Cred/API_Key.txt")

api_service_name = "youtube"
api_version = "v3"
api_key = f_API.readlines()

youtube = build(api_service_name, api_version, developerKey=api_key)

def catch_video_comments(video_id,comments_wanted):# 最大评论数量不能大于100条
    comments_list = []
    next_page_token = None
    while len(comments_list) < comments_wanted:
        request = youtube.commentThreads().list(
            part = "snippet",
            videoId = video_id,
            order = "relevance",     # 按最相关排序
            pageToken = next_page_token,
            textFormat = "plainText"
        )

        response = request.execute()
    
        for item in response['items']:
            top_comment = item["snippet"]["topLevelComment"]["snippet"]
            comments_list.append({
                "author": top_comment.get("authorDisplayName"),
                "text": top_comment.get("textDisplay"),
                "publishedAt": top_comment.get("publishedAt"),
                "likeCount": top_comment.get("likeCount")
            })
        
        next_page_token = response['nextPageToken'] #翻页token，翻不动了就停
        if not next_page_token:
            break
    
    with open('./Q4_comments.csv','w',encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=["author", "text", "publishedAt", "likeCount"])
        writer.writeheader()
        writer.writerows(comments_list[:comments_wanted])

if __name__ == '__main__':
    catch_video_comments(video_id='9bZkp7q19f0',comments_wanted=30)


