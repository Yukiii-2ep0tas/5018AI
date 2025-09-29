from googleapiclient.discovery import build
import json

f_API = open("./Cred/API_Key.txt")

def catch_channel_data(channel_id):
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

def get_description(json_filename):
    with open(f"./Saves/{json_filename}") as f:
        description = json.load(f)
        print(description["items"][0]['snippet']['description'])
    return 0

def catch_playlist_data(channel_id,playlist_id):
    api_service_name = "youtube"
    api_version = "v3"

    api_key = f_API.readlines()

    youtube = build(api_service_name, api_version, developerKey=api_key)

    request = youtube.playlists().list(
        channelID = channel_id,
        playlistID = playlist_id,
        part = "snippet,contentDetails"
    )

    respons = request.execute()

if __name__ == "__main__":
    get_description("Disney Channel Animation_snippet.json")
    catch_playlist_data("UCsT0YIqwnpJCM-mx7-gSA4Q")
