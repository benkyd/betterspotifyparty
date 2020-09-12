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
currentID = nowplaying['item']['uri']

with open('playedtracks.csv', 'a', newline='') as csvfile:
    lastplayedwrite = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    lastplayedwrite.writerow(currentID)

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
        with open('playedtracks.csv', newline='') as csvfile:
            recentlyplayed = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in recentlyplayed:
                recenttracks = row
            lines = len(list(recentlyplayed))
        return [recenttracks, lines]

    getLastPlayed = getLastPlayed()
    recenttracks = getLastPlayed[0]
    songsplayedlength = getLastPlayed[1]

    def lastplayedtrack():
        lastplayedpos = int((songsplayedlength -1))
        lasttrack = recenttracks[lastplayedpos]
        return lasttrack

    lasttrack = lastplayedtrack()

    def pastrecc():
        pastrecommendation = sp.recommendations(seed_tracks=lasttrack)
        pastrecommendedtracks = pastrecommendation["tracks"]["URI"]
        return pastrecommendedtracks

    pastrecommendations = pastrecc()

    def add_last_to_queue():
        sp.add_to_queue(pastrecommendations)