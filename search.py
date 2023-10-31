import requests

SPOTIFY_API_BASE_URL = 'https://api.spotify.com/v1/'

access_token = input('your_access_token? ')

headers = {
    'Authorization': f'Bearer {access_token}'
}

# Input: Song name to search for
song_name = input("Enter the song name you wanna to search for: ")

search_url = f'{SPOTIFY_API_BASE_URL}search'
params = {
    'q': song_name,
    'type': 'track',
    'limit': 10  # max number of tracks fetched from Spotify
}
response = requests.get(search_url, params=params, headers=headers)

if response.status_code == 200:
    # Successfully retrieved search results
    search_results = response.json()

    # Process the search results as needed
    if 'tracks' in search_results:
        for track in search_results['tracks']['items']:
            print(f"Track Name: {track['name']}")
            print(
                f"Artist: {', '.join([artist['name'] for artist in track['artists']])}")
            print(f"Album: {track['album']['name']}")
            print()
    else:
        print("No matching tracks found.")

else:
    print(f"Failed to perform the search. Status Code: {response.status_code}")
