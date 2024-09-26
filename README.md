# PLAYLIST CONVERTER
#### Video Demo:
https://www.youtube.com/watch?v=4XtdfHrbKWs
#### Description:
The Playlist Converter: YouTube to Spotify is a Python-based application that automates the transfer of playlists from YouTube to Spotify. The project leverages the YouTube Data API to extract song titles from a YouTube playlist and the Spotify Web API to create a corresponding playlist in a user's Spotify account. The goal is to save users time by eliminating the need to manually recreate playlists between platforms.

This project consists of several key components, each encapsulated in functions that perform specific tasks in the conversion process. The core functionality revolves around extracting metadata from YouTube, searching for the corresponding songs in Spotify, and adding those songs to a new playlist.

### Functions:
**main():** This function orchestrates the entire process. It prompts the user for necessary inputs, such as the name of the YouTube playlist to convert, and then coordinates the extraction, search, and playlist creation processes.

**get_youtube_playlist(playlist_id, api_key):** This function gets all the tracks in the youtube playlist and returns them. Requires The YouTube playlist ID and YouTube API key.

**spotify_search(title, artist):** Queries the Spotify Web API to find matching tracks based on the song title and artist name. It returns the Spotify track IDs of matching songs, which are later added to the playlist.

**spotify_playlist_create(user_id, playlist_name):** Creates a new Spotify playlist under the specified user's account. It uses the Spotify Web API to generate the playlist and returns the new playlist’s ID for further manipulation.

**spotify_add_to_playlist(playlist_id, items):** Adds all the tracks in the items list.

## Key Design Choices:
To ensure accuracy, this project emphasizes flexibility in querying Spotify. When possible, both the song title and artist are used to refine search results, but the system also handles cases where artist data is missing. Error handling is integrated to skip songs that cannot be found, while notifying users of any discrepancies.

This tool simplifies the tedious task of manually transferring playlists, providing an efficient solution for users who switch between music platforms regularly. By leveraging well-documented APIs and robust error handling, this converter is designed to be both practical and reliable for end users.
