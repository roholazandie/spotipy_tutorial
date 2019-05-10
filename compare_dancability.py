import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from datetime import datetime
import matplotlib.pyplot as plt

client_id = "c56c4db0897c4a13b1f9ee85712f4644"
client_secret = "1086bd8553cb4747880aaba52f6432a7"

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
token = client_credentials_manager.get_access_token()

sp = spotipy.Spotify(auth=token)


sasy_results = sp.search(q='sasy', limit=50)
aziz_results = sp.search(q='aziz weysi', limit=50)

sasy_infos = {}
for result in sasy_results["tracks"]["items"]:
    if "album" in result:
        try:
            release_date = datetime.strptime(result["album"]["release_date"], '%Y-%m-%d')
        except:
            continue
    track_id = result["id"]
    sasy_infos[track_id] = release_date


aziz_infos = {}
for result in aziz_results["tracks"]["items"]:
    if "album" in result:
        try:
            release_date = datetime.strptime(result["album"]["release_date"], '%Y-%m-%d')
        except:
            continue
    track_id = result["id"]
    aziz_infos[track_id] = release_date



sasy_track_features = sp.audio_features(sasy_infos.keys())
aziz_track_features = sp.audio_features(aziz_infos.keys())

sasy_danceabilities = {feature["id"]: feature["danceability"] for feature in sasy_track_features}
aziz_danceabilities = {feature["id"]: feature["danceability"] for feature in aziz_track_features}


print(sum(sasy_danceabilities.values()))
print(sum(aziz_danceabilities.values()))

sasy_danceabilities_by_date = []
for track_id in sasy_infos.keys():
    date = sasy_infos[track_id]
    danceability = sasy_danceabilities[track_id]
    sasy_danceabilities_by_date.append((date, danceability))

aziz_danceabilities_by_date = []
for track_id in aziz_infos.keys():
    date = aziz_infos[track_id]
    danceability = aziz_danceabilities[track_id]
    aziz_danceabilities_by_date.append((date, danceability))


sasy_danceabilities_by_date.sort(key=lambda r: r[0])
aziz_danceabilities_by_date.sort(key=lambda r: r[0])


sasy_dates = [item[0] for item in  sasy_danceabilities_by_date]
sasy_danceabilities = [item[1] for item in  sasy_danceabilities_by_date]
plt.plot(sasy_dates, sasy_danceabilities)
plt.show()


aziz_dates = [item[0] for item in  aziz_danceabilities_by_date]
aziz_danceabilities = [item[1] for item in  aziz_danceabilities_by_date]
plt.plot(aziz_dates, aziz_danceabilities)
plt.show()