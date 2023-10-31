import base64
import requests

# Spotify API credentials- you can get them from here https://developer.spotify.com/documentation/web-api/tutorials/getting-started
SPOTIFY_CLIENT_ID = 'SPOTIFY_CLIENT_ID'
SPOTIFY_CLIENT_SECRET = 'SPOTIFY_CLIENT_SECRET'
# Redirect URI set in your Spotify App
SPOTIFY_REDIRECT_URI = 'http://localhost:3000/'

SCOPE = 'user-library-read user-read-email'

auth_header = base64.b64encode(
    f"{SPOTIFY_CLIENT_ID}:{SPOTIFY_CLIENT_SECRET}".encode()).decode()

auth_url = f"https://accounts.spotify.com/authorize?client_id={SPOTIFY_CLIENT_ID}&response_type=code&redirect_uri={SPOTIFY_REDIRECT_URI}&scope={SCOPE}"
print(
    f"1. Please log in to Spotify and grant access by visiting the following URL:\n{auth_url}")
authorization_code = input(
    "2. After granting access, copy the URL you are redirected to and paste it here: ")

authorization_code = authorization_code.split("code=")[1]

token_url = "https://accounts.spotify.com/api/token"
token_data = {
    'grant_type': 'authorization_code',
    'code': authorization_code,
    'redirect_uri': SPOTIFY_REDIRECT_URI,
}
token_headers = {
    'Authorization': f'Basic {auth_header}',
}
token_response = requests.post(
    token_url, data=token_data, headers=token_headers)
token_info = token_response.json()

if 'access_token' in token_info:
    access_token = token_info['access_token']
    # Store the access token securely and use it to access Spotify data
    print(f"Access Token: {access_token}")
    # Implementing my logic here (from other files)
else:
    print("Error in retrieving access token.")
