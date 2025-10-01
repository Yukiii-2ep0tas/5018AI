from googleapiclient.discovery import build
import json
import re

f_API = open("./Cred/API_Key.txt")

def catch_channel_data(channel_id):#获取频道数据并保存到json
    api_service_name = "youtube"
    api_version = "v3"

    api_key = f_API.readlines()

    youtube = build(api_service_name, api_version, developerKey=api_key)

    request = youtube.channels().list(
        part="snippet,statistics",
        id = channel_id
    )
    response = request.execute()

    channel_name = response['items'][0]['snippet']['title']

    with open(f"./Saves/{channel_name}_snippet.json","w",encoding="utf-8") as f:
        json.dump(response,f,indent=4)
    return 0

def get_description(json_filename):#从保存的json文件中获取频道简介
    with open(f"./Saves/{json_filename}") as f:
        description = json.load(f)["items"][0]['snippet']['description']
        print(description)
    return description

def get_playlist_detail(json_filename,if_detailed):
    with open(f"./Saves/{json_filename}") as f:
        playlists = json.load(f)
        playlist_amount = playlists['pageInfo']["totalResults"]
        print(f"Total amount of playlists is :{playlist_amount}")
        if if_detailed:
            ordinal = 1
            for item in playlists['items']:
                create_date = re.match(r'^(.*?)T', item['snippet']['publishedAt']).group(1)
                playlist_name = item['snippet']['title']
                print(f'{ordinal}.Playlist Name is {playlist_name} and was created at {create_date}')
                ordinal += 1
    return 0

def catch_channel_playlist_data(channel_id):
    api_service_name = "youtube"
    api_version = "v3"

    api_key = f_API.readlines()

    youtube = build(api_service_name, api_version, developerKey=api_key)

    request = youtube.playlists().list(
        part="contentDetails,player,snippet,status",
        channelId=channel_id,
        maxResults=10
    )
    response = request.execute()
    with open(f"./Saves/{channel_id}_snippet.json","w",encoding="utf-8") as f:
        json.dump(response,f,indent=4)

def get_channel_playlist_detail(json_filename,if_detailed):#读取保存的json文件并输出该频道播放列表的总数
    with open(f"./Saves/{json_filename}") as f:
        playlists = json.load(f)
        playlist_amount = playlists['pageInfo']["totalResults"]
        print(f"Total amount of playlists is :{playlist_amount}")
        if if_detailed:#通过if detailed 参数控制是否输出播放列表中每个视频的信息
            ordinal = 1
            for item in playlists['items']:
                create_date = re.match(r'^(.*?)T', item['snippet']['publishedAt']).group(1)
                playlist_name = item['snippet']['title']
                print(f'{ordinal}.Playlist Name is {playlist_name} and was created at {create_date}')
                ordinal += 1
    return 0

def catch_single_playlist_detail(playlist_id):#输入指定的单个播放列表id，保存其信息到json文件
    
    api_service_name = "youtube"
    api_version = "v3"

    api_key = f_API.readlines()

    all_items = []
    next_page_token = None #播放列表比较长，需要翻页token
    
    youtube = build(api_service_name, api_version, developerKey=api_key)

    while True:#循环查询列表内视频
        request = youtube.playlistItems().list(
            part="contentDetails,snippet",
            playlistId=playlist_id,
            maxResults=50,
            pageToken = next_page_token
        )

        response = request.execute()

        all_items.extend(response.get('items',[]))
        next_page_token=response.get('nextPageToken')
        if not next_page_token:
            break
    with open(f'./Saves/{playlist_id}_playlist_data.json',"w",encoding="utf-8") as f:
        json.dump(all_items,f,indent=4)


if __name__ == "__main__":
    # get_description("Disney Channel Animation_snippet.json")
    # catch_playlist_data(channel_id="UCsT0YIqwnpJCM-mx7-gSA4Q") #catch TS'channel
    # catch_channel_playlist_data(channel_id="UC2jIjRE_1uvHNpRH3BSwu9Q") #catch CUHK MBA Channel
    # get_channel_playlist_detail(json_filename='UC2jIjRE_1uvHNpRH3BSwu9Q_snippet.json',if_detailed=1)
    # catch_single_playlist_detail(playlist_id="PLFEgnf4tmQe-thFfkU9EVKQoB-7r6aLXD") #catch peppa pig's playlist
    # catch_single_playlist_detail(playlist_id='PLOXw6I10VTv9DFXRidukLC2hgAAkmexWx') #catch OpenAI's playlist