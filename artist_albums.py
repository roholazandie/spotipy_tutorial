import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


def get_artist(name):
    results = sp.search(q='artist:' + name, type='artist')
    items = results['artists']['items']
    if len(items) > 0:
        return items[0]
    else:
        return None

def show_artist_albums(artist):
    albums = []
    results = sp.artist_albums(artist['id'], album_type='album')
    albums.extend(results['items'])
    while results['next']:
        results = sp.next(results)
        albums.extend(results['items'])
    seen = set() # to avoid dups
    albums.sort(key=lambda album:album['name'].lower())
    for album in albums:
        name = album['name']
        if name not in seen:
            print((' ' + name))
            seen.add(name)


if __name__ == '__main__':
    client_id = "c56c4db0897c4a13b1f9ee85712f4644"
    client_secret = "1086bd8553cb4747880aaba52f6432a7"

    client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
    token = client_credentials_manager.get_access_token()

    sp = spotipy.Spotify(auth=token)

    artist = get_artist("sasy")
    if artist:
        show_artist_albums(artist)