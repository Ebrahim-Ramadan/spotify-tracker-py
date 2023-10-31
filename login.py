import base64
import requests

# Spotify API credentials
SPOTIFY_CLIENT_ID = '2059e72499f349649fe1b70cd7ec8be2'
SPOTIFY_CLIENT_SECRET = '24724924bdbc4db29f7e3698ea6e4542'
# Redirect URI set in your Spotify App
SPOTIFY_REDIRECT_URI = 'http://localhost:3000/'

# Scope: Define what access you need from the user's Spotify account
SCOPE = 'user-library-read user-read-email'

# Base64 encode the client ID and client secret for authentication
auth_header = base64.b64encode(
    f"{SPOTIFY_CLIENT_ID}:{SPOTIFY_CLIENT_SECRET}".encode()).decode()

# Get authorization code from the user
auth_url = f"https://accounts.spotify.com/authorize?client_id={SPOTIFY_CLIENT_ID}&response_type=code&redirect_uri={SPOTIFY_REDIRECT_URI}&scope={SCOPE}"
print(
    f"1. Please log in to Spotify and grant access by visiting the following URL:\n{auth_url}")
authorization_code = input(
    "2. After granting access, copy the URL you are redirected to and paste it here: ")

# getting the authorization code from the URL
authorization_code = authorization_code.split("code=")[1]

# exchnage the authorization code for an access token
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
