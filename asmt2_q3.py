import json
from googleapiclient.discovery import build
import isodate
import time

f_API = open("./Cred/API_Key.txt")

api_service_name = "youtube"
api_version = "v3"
api_key = f_API.readlines()

youtube = build(api_service_name, api_version, developerKey=api_key)



def get_channel_name_by_playlist(playlist_id):
    with open(f"./Saves/{playlist_id}_playlist_data.json") as f:
        playlist_items = json.load(f)
    channel_name = playlist_items[0]['snippet']['channelTitle']
    print(f'this playlist belongs to the channel : {channel_name}')

def get_playlist_items(playlist_id):
    with open(f"./Saves/{playlist_id}_playlist_data.json") as f:
        playlist_items = json.load(f)
    
    video_ordinal = 1
    video_id_list = []
    for video_item in playlist_items :
        video_item_title = video_item['snippet']['title']
        video_item_id = video_item['contentDetails']['videoId']
        # print(f'{video_ordinal}. {video_item_title} and its ID is {video_item_id}')
        video_ordinal += 1
        video_id_list.append(video_item_id)
    
    return video_id_list

def catch_video_data_by_id(video_id): #获取单个视频的snippet,statistics等数据
    
    request = youtube.videos().list(
        part = 'snippet,statistics,contentDetails',
        id = video_id
    )
    response = request.execute()
    #with open('./test.json','w',encoding='utf-8') as f:    #### 用于产生例子，废弃
        #json.dump(response,f,indent=4)
    #return response
    return response

def catch_video_item_by_playlist(playlist_id):
    video_id_list = get_playlist_items(playlist_id=playlist_id)
    for video_id in video_id_list:
        video_data = catch_video_data_by_id(video_id)
        video_title = video_data['items'][0]['snippet']['title']
        video_view_count = video_data['items'][0]['statistics']['viewCount']

        ##评论区计数需要判断
        if 'commentCount' in video_data['items'][0]['statistics']:
            video_comment_count = video_data['items'][0]['statistics']['commentCount']
        else:
            video_comment_count = 0

        ##视频时长需要转换
        video_content_details = video_data['items'][0]['contentDetails']
        duration_str = video_content_details.get('duration')
        duration = int(isodate.parse_duration(duration_str).total_seconds())
        print(
            f"Info of the video_id = {video_id}: \n"
            f"Title : {video_title} \n"
            f"View Count : {video_view_count} \n"
            f"Comment Count :{video_comment_count} \n"
            f"Duration :{duration} \n" 
        )
    return 0


if __name__ == '__main__':
    # get_channel_name_by_playlist('PLFEgnf4tmQe-thFfkU9EVKQoB-7r6aLXD') print peppy's channel name
    # get_playlist_items('PLOXw6I10VTv9DFXRidukLC2hgAAkmexWx')
    # catch_video_data_by_id('DQacCB9tDaw')
    catch_video_item_by_playlist('PLOXw6I10VTv9DFXRidukLC2hgAAkmexWx')