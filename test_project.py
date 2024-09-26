import pytest

# Placeholder data to simulate function outputs
def create_query(title, artist=None):
    if artist:
        return f"title:{title} artist:{artist}"
    return f"title:{title}"

def spotify_search(title, artist):
    if title == "Blinding Lights" and artist == "The Weeknd":
        return "1VdZ0vKfR5jneCmWIUAMxK"  # Simulated track ID
    return None

def spotify_playlist_create(user_id, playlist_name):
    return "mockPlaylistId"  # Simulated playlist ID

def spotify_add_to_playlist(playlist_id, items):
    return True  # Simulated success


# Test functions
def test_create_query_with_title_and_artist():
    query = create_query("Blinding Lights", "The Weeknd")
    assert query == "title:Blinding Lights artist:The Weeknd"

def test_create_query_with_title_only():
    query = create_query("Blinding Lights")
    assert query == "title:Blinding Lights"

def test_spotify_search_valid():
    result = spotify_search("Blinding Lights", "The Weeknd")
    assert result == "1VdZ0vKfR5jneCmWIUAMxK"

def test_spotify_search_invalid():
    result = spotify_search("Unknown Song", "Unknown Artist")
    assert result is None

def test_spotify_playlist_create():
    playlist_id = spotify_playlist_create("user_id", "Test Playlist")
    assert playlist_id == "mockPlaylistId"

def test_spotify_add_to_playlist():
    result = spotify_add_to_playlist("mockPlaylistId", ["1VdZ0vKfR5jneCmWIUAMxK"])
    assert result is True
