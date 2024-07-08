from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth


CLIENT_ID = Your Client_ID
CLIENT_SECERT = Your Clieni_Secret

year = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{year}")
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
song_names_span = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_span]
# print(song_nam)

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret= CLIENT_SECERT,
        show_dialog=True,
        cache_path="token.txt",
        # username="Vaishnavi Choubey",
    )
)
user_id = sp.current_user()["id"]

song_uris = []
yr = year.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{yr}", type="track")
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
playlist = sp.user_playlist_create(user=user_id, name=f"{year} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

print(f"Playlist '{year} Billboard 100' created successfully!")
