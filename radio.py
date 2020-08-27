import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

os.environ['SPOTIPY_CLIENT_ID'] = '1071f72324a14278af0998dad4eda1f8'  # from my dash
os.environ['SPOTIPY_CLIENT_SECRET'] = 'c4eb3046229241958dee65273e505f86'  # from my dash
os.environ['SPOTIPY_REDIRECT_URI'] = 'https://localhost/api/auth/'
scope = "user-library-read user-read-currently-playing user-modify-playback-state user-read-playback-state"  #
# provides relevant scopes to auth

OAuth = SpotifyOAuth(scope=scope,
                     redirect_uri='https://localhost/api/auth/',
                     cache_path='../cache.txt')
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


