import json
from googleapiclient.discovery import build

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
        print(f'{video_ordinal}. {video_item_title} and its ID is {video_item_id}')
        video_ordinal += 1
        video_id_list.append(video_item_id)
    
    return video_id_list

def catch_video_data_by_id(video_id):
    api_service_name = "youtube"
    api_version = "v3"

    api_key = f_API.readlines()

    youtube = build(api_service_name, api_version, developerKey=api_key)
    

if __name__ == '__main__':
    # get_channel_name_by_playlist('PLFEgnf4tmQe-thFfkU9EVKQoB-7r6aLXD') print peppy's channel name
    get_playlist_items('PLOXw6I10VTv9DFXRidukLC2hgAAkmexWx')