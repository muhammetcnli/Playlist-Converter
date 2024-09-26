import requests
from dotenv import load_dotenv
import json
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import base64

load_dotenv()

SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')
YOUTUBE_PLAYLIST_ID= os.getenv('YOUTUBE_PLAYLIST_ID')


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri="http://localhost/",
    scope="playlist-modify-public"
))

def main():

    load_dotenv()  # Load environment variables from .env
    '''YOUTUBE_API_KEY =YOUTUBE_API_KEY
    YOUTUBE_PLAYLIST_ID =YOUTUBE_PLAYLIST_ID
    SPOTIFY_CLIENT_SECRET =SPOTIFY_CLIENT_SECRET'''
    SPOTIFY_CLIENT_ID = sp.me()['id']


    songs = get_youtube_playlist(YOUTUBE_PLAYLIST_ID, YOUTUBE_API_KEY)
    track_uris = []
    spotify_playlist_id = spotify_playlist_create(SPOTIFY_CLIENT_ID, input("Playlist name: "))
    for title, artist in songs:
        track_id = spotify_search(title, artist)
        if track_id:
            track_uri = "spotify:track:" + track_id
            track_uris.append(track_uri)
            if len(track_uris) == 20:
                spotify_add_to_playlist(spotify_playlist_id, track_uris)
                track_uris = []

    spotify_add_to_playlist(spotify_playlist_id, track_uris)


def get_youtube_playlist(playlist_id, api_key):
    '''
    This method gets all the possible songs from the youtube playlist.
    Requires playlist_id and api_key
    '''
    # This is the initial page pull
    songs = []
    url = f"https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId={playlist_id}&maxResults=50&key={api_key}"
    response = requests.get(url)
    data = response.json()

    # here we look all for title and artist if not found we continue
    for item in data['items']:
        try:
            title = item['snippet']['title']
            artist = item["snippet"]['videoOwnerChannelTitle']
            songs.append((title, artist))
        except KeyError:
            continue

    nextPageToken = data["nextPageToken"]

    # Now we have 50 songs, we have to get to the next page using the nextPageToken
    while True:
        url = f"https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId={playlist_id}&maxResults=50&pageToken={nextPageToken}&key={api_key}"
        response = requests.get(url)
        data = response.json()
        # geting the next pages constantly, when there is no next page, in the last page, the program should break the while loop
        try:
            nextPageToken = data["nextPageToken"]

            for item in data["items"]:
                try:
                    title = item["snippet"]["title"]
                    artist = item["snippet"]['videoOwnerChannelTitle']
                    songs.append((title, artist))
                except KeyError:
                    continue
        except:
            break
    return songs


def spotify_search(title, artist):
    '''
    This method searches for the songs in spotify.
    Requiers title and artist
    '''

    query = f"title:{title}"
    result = sp.search(q=query, limit=1, type="track")
    if result["tracks"]["items"]:
        return result["tracks"]["items"][0]["id"]


def spotify_playlist_create(user_id, playlist_name):
    playlist = sp.user_playlist_create(user_id, playlist_name, True, False, "This is a automated playlist from youtube.")
    return playlist["id"]


def spotify_add_to_playlist(playlist_id, items):
    add = sp.playlist_add_items(playlist_id, items)

if __name__ == "__main__":
    main()
