import requests

SPOTIFY_API_BASE_URL = 'https://api.spotify.com/v1/'

access_token = input('your_access_token?')

headers = {
    'Authorization': f'Bearer {access_token}'
}

# fetch the my saved tracks
saved_tracks_url = f'{SPOTIFY_API_BASE_URL}me/tracks'
response = requests.get(saved_tracks_url, headers=headers)

if response.status_code == 200:
    saved_tracks_data = response.json()

    for track in saved_tracks_data['items']:
        print(f"Track Name: {track['track']['name']}")
        print(
            f"Artist: {', '.join([artist['name'] for artist in track['track']['artists']])}")
        print(f"Album: {track['track']['album']['name']}")
        print()

else:
    print(
        f"Failed to retrieve saved tracks. Status Code: {response.status_code}")
