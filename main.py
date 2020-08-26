import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
import json

os.environ['SPOTIPY_CLIENT_ID'] = ''  # from my dash
os.environ['SPOTIPY_CLIENT_SECRET'] = ''  # from my dash
os.environ['SPOTIPY_REDIRECT_URI'] = 'https://localhost/api/auth/'
scope = "user-library-read user-read-currently-playing user-modify-playback-state user-read-playback-state"

OAuth = SpotifyOAuth(scope=scope,
                     redirect_uri='https://localhost/api/auth/',
                     cache_path='../cache.txt')
token = OAuth.get_cached_token()
sp = spotipy.Spotify(auth_manager=OAuth)


def getPlaying():
    userplaying = sp.current_playback()
    with open("data_file.json", "w") as write_file:
        json.dump(userplaying, write_file)
    with open("data_file.json", "r"):
        json.loads(userplaying)
    return userplaying

UserPlaying = getPlaying()
print(UserPlaying)
