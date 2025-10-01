import json
def get_channel_name_by_playlist(playlist_id):
    with open(f"./Saves/{playlist_id}_playlist_data.json") as f:
        playlist_items = json.load(f)
    channel_name = playlist_items[0]['snippet']['channelTitle']
    print(f'this playlist belongs to the channel : {channel_name}')

def get_playlist_items(playlist_id):
    with open(f"./Saves/{playlist_id}_playlist_data.json") as f:
        playlist_items = json.load(f)
    

if __name__ == '__main__':
    print_channel_name_by_playlist('PLFEgnf4tmQe-thFfkU9EVKQoB-7r6aLXD')