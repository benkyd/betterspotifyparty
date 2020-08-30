import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv, find_dotenv
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
token = OAuth.get_cached_token()
sp = spotipy.Spotify(auth_manager=OAuth)


# Need to implement a callback, taking the assigned token and returning it to the program, rather than entering URL
# each time for auth

def getPlaying():  # gets the currently playing track for the signed in user
    userplaying = sp.current_playback()
    playingdata = userplaying['item']['id']
    return playingdata


playingtrackID = getPlaying()


#def getFeatures():  # calls the API to get the features of a given track ID
  #  featuresdata = sp.audio_features(playingtrackID)
   # dance = featuresdata['danceability']
  #  energy = featuresdata['energy']
  #  valence = featuresdata['valence']
  #  tempo = featuresdata['tempo']
 #   features = [dance, energy, valence, tempo]
  #  return [features]


#audioFeatures = []
#audioFeatures = getFeatures()
#dance = audioFeatures[0]
#energy = audioFeatures[1]
#valence = audioFeatures[2]
#tempo = audioFeatures[3]


userlike = input("Do you like this track? ")
if userlike == "Yes" or userlike == "yes":
    seedtracks = playingtrackID


def getRecommended():
    recommendations = sp.recommendations(seed_tracks=seedtracks)
    recommendedtracks = recommendations['tracks']['id']
    return [recommendedtracks]


recommmendedtracks = [] = getRecommended()


