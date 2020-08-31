import os

import spotipy
from dotenv import load_dotenv, find_dotenv
from spotipy.oauth2 import SpotifyOAuth

load_dotenv(find_dotenv())

SPOTIPY_CLIENT_ID = os.getenv('SPOTIFY_APP_ID')
SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIFY_APP_TOKEN')
SPOTIPY_REDIRECT_URI = os.getenv('SPOTIFY_REDIRECT_URI')
scope = "user-library-read user-read-currently-playing user-modify-playback-state user-read-playback-state"  #
# provides relevant scopes to auth

OAuth = SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                     client_secret=SPOTIPY_CLIENT_SECRET,
                     scope=scope,
                     redirect_uri=SPOTIPY_REDIRECT_URI,
                     cache_path='../../cache.txt',
                     )
token = OAuth.get_access_token("200")
sp = spotipy.Spotify(auth_manager=OAuth)


# Need to implement a callback, taking the assigned token and returning it to the program, rather than entering URL
# each time for auth

def checkplaying():
    playing = sp.current_playback()
    isplaying = bool(playing["is_playing"])
    return isplaying

isplaying = checkplaying()

while isplaying:

    def getPlaying():  # gets the currently playing track for the signed in user
        userplaying = sp.current_playback()
        playingdata = userplaying['item']['id']
        return playingdata


    playingtrackID = getPlaying()

    # def getFeatures():  # calls the API to get the features of a given track ID
    #  featuresdata = sp.audio_features(playingtrackID)
    # dance = featuresdata['danceability']
    #  energy = featuresdata['energy']
    #  valence = featuresdata['valence']
    #  tempo = featuresdata['tempo']
    #   features = [dance, energy, valence, tempo]
    #  return [features]


    # audioFeatures = []
    # audioFeatures = getFeatures()
    # dance = audioFeatures[0]
    # energy = audioFeatures[1]
    # valence = audioFeatures[2]
    # tempo = audioFeatures[3]

    seedtracks = []

    userlike = input("Do you like this track? ")
    if userlike == "Yes" or userlike == "yes":
        seedtracks.append(playingtrackID)


    def getRecommended():
        recommendations = sp.recommendations(seed_tracks=seedtracks)
        recommendedtracks = recommendations["tracks"][(len(seedtracks))]["id"]
        return [recommendedtracks]


    recommmendedtracks = []
    recommmendedtracks = getRecommended()


    def recommendedNames():
        search = sp.tracks(recommmendedtracks)
        reccnames = search["tracks"][0]["id"]
        return [reccnames]


    reccnames = []
    reccnames.append(recommendedNames())

    print(reccnames)
