import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id = "c56c4db0897c4a13b1f9ee85712f4644"
client_secret = "1086bd8553cb4747880aaba52f6432a7"

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
token = client_credentials_manager.get_access_token()
sp = spotipy.Spotify(auth=token)

results = sp.search(q='sasy', limit=20)
for i, t in enumerate(results['tracks']['items']):
    print(' ', i, t['name'])