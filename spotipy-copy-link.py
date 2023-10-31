import spotipy  # this feature using sopipy (same thing)
from spotipy.oauth2 import SpotifyClientCredentials

client_id = 'client_id'
client_secret = 'client_secret'

client_credentials_manager = SpotifyClientCredentials(
    client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

song_name = "What It Is"
results = sp.search(q='track:' + song_name, type='track', limit=1)
print('results', results)

if results['tracks']['items']:
    song = results['tracks']['items'][0]
    song_link = song['external_urls']['spotify']
    print(f"Song Name: {song_name}")
    print(f"Spotify Link: {song_link}")
else:
    print(f"No results found for '{song_name}'")
