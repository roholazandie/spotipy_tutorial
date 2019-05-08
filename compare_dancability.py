import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


client_id = "c56c4db0897c4a13b1f9ee85712f4644"
client_secret = "1086bd8553cb4747880aaba52f6432a7"

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
token = client_credentials_manager.get_access_token()

sp = spotipy.Spotify(auth=token)

sp.search(q='persian', type='genre')
sasy_results = sp.search(q='sasy', limit=20)
shajarian_results = sp.search(q='shajarian', limit=20)

sasy_track_ids = []
for result in sasy_results["tracks"]["items"]:
    track_id = result["id"]
    sasy_track_ids.append(track_id)



shajarian_track_ids = []
for result in shajarian_results["tracks"]["items"]:
    track_id = result["id"]
    shajarian_track_ids.append(track_id)

sasy_track_features = sp.audio_features(sasy_track_ids)
shajarian_track_features = sp.audio_features(shajarian_track_ids)

sasy_danceabilities = [feature['danceability'] for feature in sasy_track_features]
shajarian_danceabilities = [feature['danceability'] for feature in shajarian_track_features]

print(sum(sasy_danceabilities))
print(sum(shajarian_danceabilities))