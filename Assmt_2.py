from googleapiclient.discovery import build

f_API = open("./Cred/API_Key.txt")

def catch(Username):
    api_service_name = "youtube"
    api_version = "v3"

    api_key = f_API.readlines()

    # Build the YouTube service using API key
    youtube = build(api_service_name, api_version, developerKey=api_key)

    # Make a request to get channel details
    request = youtube.channels().list(
        part="snippet,contentDetails,statistics",
        forUsername=Username
    )
    response = request.execute()
    print(response)

if __name__ == "__main__":
    catch("GoogleDevelopers")
