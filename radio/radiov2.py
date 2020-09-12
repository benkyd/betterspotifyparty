import os
import csv
import spotipy
from dotenv import load_dotenv, find_dotenv
from spotipy.oauth2 import SpotifyOAuth

currentID = None
uri = None
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


nowplaying = sp.current_playback()
currentID = nowplaying['item']['id']
currentURI = nowplaying['item']['uri']

f = open("playedtracksID.txt", "a") # ID used for recommendations
f.write(currentID + "\n")
f.close()

g = open("playedtracksURI.txt", "a") # URI used for adding to queue
g.write(currentURI + "\n")
g.close()

userlikes = input("Do you like this track? ")

if userlikes == "yes" or userlikes == "y" or userlikes == "Yes":

    def getPlaying():  # gets the currently playing track for the signed in user
        userplaying = sp.current_playback()
        playingdata = userplaying['item']['id']
        return playingdata  # returns ID of currently playing track


    playingtrackID = getPlaying()
    seedtracks= []
    seedtracks.append(playingtrackID)

    def getRecommended():  # uses an API call to seed recommendations, then spotify returns a .json containing the reccomendations
        recommendations = sp.recommendations(seed_tracks=seedtracks)
        nexttoplay = recommendations['tracks'][00]['uri']
        return nexttoplay  # return the list of recommended tracks

    nexttoplay = getRecommended()

    sp.add_to_queue(nexttoplay)

else:
    def getLastPlayed():
        f = open("playedtracksID.txt", "r") # reads track ID of all songs
        recenttracks = f.readlines()

        num_lines = 0
        g = open("playedtracksURI.txt", "r") # reads track URI of all songs
        for line in g:
            num_lines += 1

        return [recenttracks, num_lines]

    getLastPlayed = getLastPlayed()
    recenttracks = getLastPlayed[0]
    songsplayedlength = getLastPlayed[1]

    def lastplayedtrack():
        lastplayedpos = int((songsplayedlength -1))
        lasttrack = recenttracks[lastplayedpos]
        return lasttrack

    lasttrack = lastplayedtrack()

    def pastrecc():
        pastrecommendation = sp.recommendations(seed_tracks=lasttrack) # uses track ID to seed generation
        pastrecommendedtracks = pastrecommendation["tracks"]["URI"]
        return pastrecommendedtracks

    pastrecommendations = pastrecc()

    sp.add_to_queue(pastrecommendations)