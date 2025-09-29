from googleapiclient.discovery import build
import json

f_API = open("./Cred/API_Key.txt")

def catch_snippet(Username):
    api_service_name = "youtube"
    api_version = "v3"

    api_key = f_API.readlines()

    youtube = build(api_service_name, api_version, developerKey=api_key)

    request = youtube.channels().list(
        part="snippet",
        id = "UCw7SNYrYei7F5ttQO3o-rpA"
    )
    response = request.execute()

    with open(f"./Saves/{Username}_snippet.json","w",encoding="utf-8") as f:
        json.dump(response,f,indent=4)

if __name__ == "__main__":
    catch_snippet("disneychannelanimation")
