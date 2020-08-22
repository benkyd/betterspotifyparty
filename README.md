# betterspotifyparty

A project inspired by the lacklustre implementation by both discord and spotify, of a way to listen to music collaboratively. Whilst sites exist, they are often restrictive, slow, or lack features.

## The Aim
To allow friends and family in remote areas to connect via music, without bloat or delay

To provide a better alternative to other publically available projects, at no cost to the end user

## Installation

Server requires .env variables which can be provided by enviroment variables or a .env file with the relavent configuration

It should follow this template

```
NODE_ENV="" # production / development
SPOTIFY_BASE_API="" # api.spotify.com/v1/...
SPOTIFY_APP_TOKEN="" # token from developer.spotify.com
```

## The plan
Allow a user to host a listening party, wherein the host controls the music, but can take suggestions from users. Users will also be able to vote to skip a song, requiring a majority vote to do so. Should the host wish, they can resign host position to another user. This allows a party to continue in absence, or for any other reason the user desires.


