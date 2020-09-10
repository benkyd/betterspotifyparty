import os

import spotipy
from dotenv import load_dotenv, find_dotenv
from spotipy.oauth2 import SpotifyOAuth

currentID = None
uri = None
queuepath = '/radio/queue.txt'
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


def checkplaying():  # checks if user is actually playing a track, returns true or false. Only checks if the current track is playing so always true?
    playing = sp.current_playback()
    isplaying = bool(playing["is_playing"])
    return isplaying


isplaying = checkplaying()

nowplaying = sp.current_playback()
currentID = nowplaying['item']['id']
 # currentURI = nowplaying['item']['URI']
queue_object = open(queuepath, "a")
 # queue_object.write(currentURI + "," + currentID)
queue_object.write(currentID)
queue_object.close()

read_past = open(queuepath, "r")
read_past.seek(0)
pastQueue = []
pastQueue = read_past.readlines()
pastQlength = len(pastQueue)

if pastQueue[(pastQlength - 1)] != pastQueue[(pastQlength)]:
    def getPlaying():  # gets the currently playing track for the signed in user
        userplaying = sp.current_playback()
        playingdata = userplaying['item']['id']
        playingname = userplaying["item"]["name"]
        return playingdata  # returns ID of currently playing track


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

    def getRecommended():  # uses an API call to seed recommendations, then spotify returns a .json containing the reccomendations
        recommendations = sp.recommendations(seed_tracks=seedtracks)
        recommendedtracks = recommendations["tracks"][(len(seedtracks))]["URI"]
        return [recommendedtracks]  # return the list of recommended tracks


    recommmendedtracks = []
    recommmendedtracks = getRecommended()

    # def recommendedNames():
    # search = sp.tracks(recommmendedtracks)
    # reccnames = search["tracks"][0]["id"]
    # return reccnames

    # reccnames = []
    # reccnames.append(recommmendedtracks)

    print(recommmendedtracks)


    def addtoQueue():
        sp.add_to_queue(recommmendedtracks)


else:
    print("You've already submitted feedback for this track, please wait until the next track plays")
