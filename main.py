import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
import json

os.environ['SPOTIPY_CLIENT_ID'] = '1071f72324a14278af0998dad4eda1f8'  # from my dash
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
    playingdata = userplaying['item']['id']
    return playingdata


playingtrackID = getPlaying()


def getAnalysis():
    analysisdata = sp.audio_features(playingtrackID)
    acoustic = analysisdata['acousticness']
    energy = analysisdata['energy']

    return analysisdata


userlike = input("Do you like this track? ")
if userlike == "Yes" or userlike == "yes":
    analysis = getAnalysis()
