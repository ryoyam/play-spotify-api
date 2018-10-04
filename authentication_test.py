import requests
import base64
import os

client_id = os.getenv('SPOTIPY_CLIENT_ID')
client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')


url = 'https://accounts.spotify.com/api/token'

payload = {'grant_type': 'client_credentials'}
auth_base64 = base64.urlsafe_b64encode((client_id + ':' + client_secret).encode())
auth_header_value = 'Basic ' + str(auth_base64)[2:][:-1]
headers = {
    'Authorization': auth_header_value,
    # "Content-Type": "application/x-www-form-urlencoded"
    }
r = requests.post(url, payload, headers=headers)

print(r.text)
print(auth_header_value)
